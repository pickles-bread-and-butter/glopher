package main

import (
	"glogistery/registry_server"
)

func main() {
	RunServer()
}

func RunServer() {
	registry_server.SetupRegistryServer()
	registry_server.SetupManifestWatcher()
	registry_server.StartRegistryServer()
}
