package hello_world

import (
  "context"
  "gopkg.in/yaml.v2"
  pb "hello_world/glotos"
)

func (helloWorldServer *HelloServer) UnaryCallPlugin(CallContext context.Context, HelloWordServerRequest *pb.PluginUnaryRequest) (*pb.PluginUnaryResponse, error) {
  inputMapping := make(map[string]string)
  err := yaml.Unmarshal(HelloWordServerRequest.ClientCommandFile, &inputMapping)
  var HelloWorldServerResponse *pb.PluginUnaryResponse
  if err == nil {
    responseMapping := make(map[string]string)
    responseMapping["Hello"] = inputMapping["name"]
    bytes, err := yaml.Marshal(responseMapping)
    if err == nil {
      HelloWorldServerResponse = &pb.PluginUnaryResponse{
        ServerResponseFile: bytes,
      }
    }
  }
  return HelloWorldServerResponse, err
}
