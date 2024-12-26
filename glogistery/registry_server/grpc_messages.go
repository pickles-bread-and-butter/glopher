package registry_server

import (
	"errors"
	"fmt"
	pb "glogistery/glotos"
)

func FormPluginListResponse() pb.PluginListResponse {
	PluginNames := GetPluginNames()
	PluginListReponse := pb.PluginListResponse{
		PluginNames: PluginNames}
	return PluginListReponse
}

func FormGetPluginResponse(PluginName string) (*pb.PluginGetResponse, error) {
	if Plugin, ok := Manifest.Plugins[PluginName]; ok {
		GetPluginResponse := pb.PluginGetResponse{
			PluginDef: Plugin}
		return &GetPluginResponse, nil
	} else {
		return nil, errors.New(fmt.Sprintf("No plugin %s, contact ListPlugins to see available.", PluginName))
	}
}
