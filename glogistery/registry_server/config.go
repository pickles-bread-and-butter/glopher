package registry_server

import (
	"fmt"
	"github.com/spf13/viper"
	"log"
)

func LoadConfig() {
	CurDirName := "."
	configName := "glogistery_config.yaml"
	viper.SetDefault("ManifestPath", "~/glogistery_manifest.yaml")
	viper.SetDefault("AddressToServer", 50051)
	viper.SetConfigName("glogistery_config")
	viper.SetConfigType("yaml")
	viper.AddConfigPath(CurDirName)
	if err := viper.ReadInConfig(); err != nil {
		if _, ok := err.(viper.ConfigFileNotFoundError); ok {
			log.Fatal(fmt.Sprintf("Config not found at %s/%s", CurDirName, configName))
		} else {
			log.Fatal(err)
		}
	}
	log.Println("Config file loaded, access through Viper package")
}
