// Goglistry currently only supports having a having a manifest in the form of yaml
// This yaml is intended to be in shared memory between all replicas in case of failure
// Eventually if there is enough velocity a db backed registry might be the way to go
package registry_server

import (
	"fmt"
	pb "glogistery/glotos"
	"log"
	"os"

	"buf.build/go/protoyaml"
	"github.com/fsnotify/fsnotify"
	"github.com/spf13/viper"
)

var Manifest pb.Manifest

func LoadManifest() {
	filePath := fmt.Sprintf("%s%s", viper.GetString("ManifestFilePath"), viper.GetString("ManifestFileName"))
	yamlBytes, _ := os.ReadFile(filePath)

	options := protoyaml.UnmarshalOptions{
		Path: filePath,
	}
	if err := options.Unmarshal(yamlBytes, &Manifest); err != nil {
		log.Fatal(err)
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
			  if ev.Op&fsnotify.Write == fsnotify.Write {
				  log.Println("Here")
			  }else if ev.Op&fsnotify.Rename == fsnotify.Rename {
          // In Kqueue on Mac and BSD with nvim rename == write
          log.Println(ev.Name)
          log.Println("File renamed, can no longer read")
        }
      }
		case err := <-watcher.Errors:
			log.Println("error:", err)
		}
	}
}
