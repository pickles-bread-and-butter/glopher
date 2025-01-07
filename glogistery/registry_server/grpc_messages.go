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

func FormRegisterPluginResponse(PluginRegisterRequest *pb.PluginRegisterRequest) (*pb.PluginRegisterResponse, error) {
  ManifestUpdateCodeVal, err := addOrUpdatePluginManifest(PluginRegisterRequest.PluginServiceDefinition)
  if err != nil {
    return nil, err
  }
  RegisterPluginResponse := pb.PluginRegisterResponse{
    ReponseCode: int64(*ManifestUpdateCodeVal),
    PluginAssignedUUID: PluginRegisterRequest.PluginServiceDefinition.PluginUUID,
    ResponseString: fmt.Sprint("%s", ManifestUpdateCodeVal),
  }
  return &RegisterPluginResponse, err
}

func FormPluginRemoveResponse(PluginRemoveRequest *pb.PluginRemoveRequest) (*pb.PluginRemoveResponse, error) {
  PluginRemoveCode, err := removeManifestPlugin(&PluginRemoveRequest.PluginName)
  var pntrPluginUUID *int64 = nil
  if PluginRemoveCode != nil {
    PluginUUID := int64(*PluginRemoveCode)
    pntrPluginUUID = &PluginUUID
  }
  PluginRemoveResponse := pb.PluginRemoveResponse{
    ResponseString: fmt.Sprintf("%s", PluginRemoveCode),
    PluginUUID: pntrPluginUUID,
  }
  return &PluginRemoveResponse, err
}
