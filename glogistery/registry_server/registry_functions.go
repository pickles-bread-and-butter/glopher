package registry_server

import (
	"context"
	"fmt"
	emptypb "github.com/golang/protobuf/ptypes/empty"
	pb "glogistery/glotos"
	"log"
)

func (registryServer *RegistryGRPCServer) ListPlugins(CallContext context.Context, EmptyPB *emptypb.Empty) (*pb.PluginListResponse, error) {
	ListReponse := FormPluginListResponse()
	return &ListReponse, nil
}

func (registryServer *RegistryGRPCServer) GetPlugin(CallContext context.Context, GetPluginRequest *pb.PluginGetRequest) (*pb.PluginGetResponse, error) {
	GetPluginResponse, err := FormGetPluginResponse(GetPluginRequest.PluginName)
	if err != nil {
		log.Println(fmt.Sprintf("Forming plugin response for %s caused error", GetPluginRequest.PluginName))
		log.Println(err)
	}
	return GetPluginResponse, err
}

func (registryServer *RegistryGRPCServer) RegisterPlugin(CallContext context.Context, PluginRegisterRequest *pb.PluginRegisterRequest) (*pb.PluginRegisterResponse, error) {
  RegisterPluginResponse, err := FormRegisterPluginResponse(PluginRegisterRequest)
  if err != nil {
    log.Println(fmt.Sprintf("Registering plugin %s caused error", PluginRegisterRequest.PluginServiceDefinition.PluginName))
    log.Println(err)
  }
  return RegisterPluginResponse, err
}
