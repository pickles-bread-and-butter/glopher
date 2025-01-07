// Goglistry currently only supports having a having a manifest in the form of yaml
// This yaml is intended to be in shared memory between all replicas in case of failure
// Eventually if there is enough velocity a db backed registry might be the way to go
package registry_server

import (
  "os/user"
	"fmt"
  "maps"
  "errors"
  "strings"
  "path/filepath"
	pb "glogistery/glotos"
	"log"
	"os"
  "time"

	"buf.build/go/protoyaml"
	"github.com/fsnotify/fsnotify"
	"github.com/spf13/viper"
  "gopkg.in/yaml.v2"
)

var (
  Manifest pb.Manifest
)

type ManifestUpdateCode int

const (
  PluginAdded ManifestUpdateCode = iota
  PluginUpdated
  PluginDeleted
  UpdateFailed
)

var updateNaming = map[ManifestUpdateCode]string{
  PluginAdded: "added plugin",
  PluginUpdated: "updated plugin",
  PluginDeleted: "deleted plugin",
  UpdateFailed: "failed update",
}

func (updateCode ManifestUpdateCode) String() string {
  return updateNaming[updateCode]
}

func addOrUpdatePluginManifest(pluginDef *pb.PluginDefintion) (*ManifestUpdateCode, error) {
  // check current manifest object for the plugin name (if so update)
  pluginName := pluginDef.PluginName
  _, ok := Manifest.Plugins[pluginName]
  manifestUpdateCode := ManifestUpdateCode(UpdateFailed)
  if ok {
    log.Println("Plugin exists, operation will update plugin.")
    manifestUpdateCode = ManifestUpdateCode(PluginUpdated)
  } else {
    log.Println("Plugin doesn't exist, adding fresh plugin.")
    manifestUpdateCode = ManifestUpdateCode(PluginAdded)
  }

  manifestDirPath := getUserPath(viper.GetString("ManifestFilePath"))
	manifestFilePath := filepath.Join(manifestDirPath, viper.GetString("ManifestFileName"))
  manifestMapping, err := readYamlFile(&manifestFilePath)

  if err != nil {
    log.Println(fmt.Sprintf("Failed to parse manifest file w/t err, %e", err))
    if strings.Contains(err.Error(), "File is empty can't unmarshal.") {
      log.Println("Empty manifest file, creating new manifest")
      manifestMapping = &map[string]interface{}{
        "Plugins": map[string]interface{}{},
      }
    } else {
      manifestUpdateCode = ManifestUpdateCode(UpdateFailed)
      return &manifestUpdateCode, err
    }
  }
  
  err = updateManifestMapping(manifestMapping, pluginDef)

  if err != nil {
    log.Println("Error merging manifest mapping and plugin mapping")
    manifestUpdateCode = ManifestUpdateCode(UpdateFailed)
    return &manifestUpdateCode, err
  }
  // file needs to be updated and the manifest object
  // updating the manfiest object is done automatically
  // after updating the file
  err = updateManifestFile(manifestMapping)

  return &manifestUpdateCode, err
}

func updateManifestFile(manifestMapping *map[string]interface{}) error {
  if manifestMapping == nil {
    log.Println("Null mapping can't be saved to file.")
    return errors.New("Null mapping can't be saved to file.")
  }

  yamlManifestBytes, err := yaml.Marshal(*manifestMapping)
  if err != nil {
    log.Println("Error marshalling yaml to bytes")
    return err
  }

  manifestDirPath := getUserPath(viper.GetString("ManifestFilePath"))
	manifestFilePath := filepath.Join(manifestDirPath, viper.GetString("ManifestFileName"))
  err = os.WriteFile(manifestFilePath, yamlManifestBytes, 0644)
  if err != nil {
    log.Println("Failed to write to manifest file path, %s", manifestFilePath)
    return err
  }
  return nil
}

func updateManifestMapping(manifestMapping *map[string]interface{}, pluginDef *pb.PluginDefintion) error {
  if manifestMapping == nil {
    log.Println("Null pointer for manifest mapping, internal error!")
    return errors.New("Internal error.")
  }

  pluginDefYamlBytes, _ := protoyaml.Marshal(
    pluginDef,
  )
  var pluginDefMapping map[string]interface{}
  // have to make second variable to nest inside at plugins key
  pluginsDefMapping := map[string]interface{}{
    "Plugins": map[string]interface{}{},
  }
  err := yaml.Unmarshal(pluginDefYamlBytes, &pluginDefMapping)
  pluginSpecificMap := map[string]interface{}{
    pluginDef.PluginName: pluginDefMapping,
  }
  pluginsDefMapping["Plugins"] = pluginSpecificMap

  maps.Copy(*manifestMapping, pluginsDefMapping)
  return err
}

func readYamlFile(filePath *string) (*map[string]interface{}, error){
    fileInfo, err := os.Stat(*filePath)
    if err != nil {
      if os.IsNotExist(err) {
        log.Println("%s does not exist", filePath)
      } else {
        log.Println("Error on stat file %e", err)
      }
      return nil, err
    }

    if fileInfo.Size() == 0 {
      log.Println("File is empty, cannot unmarshal to yaml.")
      return nil, errors.New("File is empty can't unmarshal.")
    }

    yamlBuffer, err := os.Open(*filePath)
    if err != nil {
      log.Println("Err opening file")
      return nil, err
    }
    defer yamlBuffer.Close()

    m := make(map[string]interface{})
    decoder := yaml.NewDecoder(yamlBuffer)
    err = decoder.Decode(&m)

    if err != nil {
      log.Println("Couldn't unmarshal file on sytax")
      return nil, err
    }
    return &m, err
}

func getUserPath(path string) string {
  var ret_path string
  if strings.HasPrefix("~/", path) {
    usr, _ := user.Current()
    dir := usr.HomeDir
    ret_path = filepath.Join(dir, path[2:])
  } else {
    log.Println("No relative path defined, returning original path.")
    ret_path = path
  }
  return ret_path
}

func LoadManifest() {
  // Potential race condition with the file system and renames, can't solve it properly because there
  // are multiple Rename emits from the fs on bsd but fsnotify doesn't make the RenamedFrom publically
  // available. Sleep compensates for the problem by waiting five seconds which should be maximum required.
  // Dog shit compensation but there's no way to compensate without building my own package
  dir_path := getUserPath(viper.GetString("ManifestFilePath"))
	filePath := filepath.Join(dir_path, viper.GetString("ManifestFileName"))
  time.Sleep(5)
  if _, err := os.Stat(filePath); err == nil {
    yamlBytes, _ := os.ReadFile(filePath)

    options := protoyaml.UnmarshalOptions{
      Path: filePath,
    }
    if err = options.Unmarshal(yamlBytes, &Manifest); err != nil {
      log.Fatal(err)
    }
  } else if errors.Is(err, os.ErrNotExist) {
    // Log out the error, wait has already compensated for race condition
    // so this should not happen.
    log.Fatal(fmt.Sprintf("Config file does not exist, %s.", filePath))
  } else {
    // Schrodingers file
    log.Fatal(fmt.Sprintf("Unknown err, %e", err))
  }
}

func GetPluginNames() []string {
	var PluginNames []string
	for PluginName, _ := range Manifest.Plugins {
		PluginNames = append(PluginNames, PluginName)
	}
	return PluginNames
}

func RegisterPlugin() {

}

func WatchManifest() {
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		panic(err)
	}

	dirPath := getUserPath(viper.GetString("ManifestFilePath"))
	manifestPath := filepath.Join(dirPath, viper.GetString("ManifestFileName"))
	err = watcher.Add(dirPath)
	if err != nil {
		panic(err)
	}

	for {
		select {
    // Mac/Nvim - Kqueue emits a create and rename on nvim writing
    // This is because nvim creates a swap file for working,
    // on write op it then renames that swap file to the original
    // file name and uses chmod and finally deletes the swap file.
    // This emits CREATE, RENAME, CREATE, CHMOD, REMOVE, CHMOD
    // in that order respecitively
		case ev := <-watcher.Events:
      if ev.Name == manifestPath {
			  if ev.Op&fsnotify.Write == fsnotify.Write || ev.Op&fsnotify.Rename == fsnotify.Rename {
          // In Kqueue on Mac and BSD with nvim rename == write
          log.Println("Manifest file changed, reloading")
          LoadManifest()
        }else if ev.Op&fsnotify.Remove == fsnotify.Remove {
          log.Fatal("Manifest file removed, critical error!")
        }
      }
		case err := <-watcher.Errors:
			log.Println("error:", err)
		}
	}
}
