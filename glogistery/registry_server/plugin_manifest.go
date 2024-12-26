// Goglistry currently only supports having a having a manifest in the form of yaml
// This yaml is intended to be in shared memory between all replicas in case of failure
// Eventually if there is enough velocity a db backed registry might be the way to go
package registry_server

import (
	"fmt"
  "errors"
	pb "glogistery/glotos"
	"log"
	"os"

	"buf.build/go/protoyaml"
	"github.com/fsnotify/fsnotify"
	"github.com/spf13/viper"
)

var Manifest pb.Manifest
var manifestReadCount int = 0

func LoadManifest() {
  // Potential race condition with the file system and renames, can't solve it properly because there
  // are multiple Rename emits from the fs on bsd but fsnotify doesn't make the RenamedFrom publically
  // available. Wait compensates as the fs write should not be more than a second
	filePath := fmt.Sprintf("%s%s", viper.GetString("ManifestFilePath"), viper.GetString("ManifestFileName"))
  if _, err := os.Stat(filePath); err == nil {
    yamlBytes, _ := os.ReadFile(filePath)

    options := protoyaml.UnmarshalOptions{
      Path: filePath,
    }
    if err = options.Unmarshal(yamlBytes, &Manifest); err != nil {
      log.Fatal(err)
    }
    manifestReadCount = 0
  } else if errors.Is(err, os.ErrNotExist) {
    // Log out the error and keep a global count, if it happens twice
    // assume the second indicates that a fatal read as there are always
    // guaranteed to be two Renames on bsd systems
    manifestReadCount += 1
    log.Println(fmt.Sprintf("Config file does not exist, %s. Have attempted to read %d times.", filePath, manifestReadCount))
    if manifestReadCount == 2 {
      log.Fatal("Attempted and failed two reads, assuming file does not exist and not a file system write known issue.")
    }
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

func WatchManifest() {
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		panic(err)
	}

	dirPath := viper.GetString("ManifestFilePath")
	manifestPath := fmt.Sprintf("%s%s", viper.GetString("ManifestFilePath"), viper.GetString("ManifestFileName"))
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
