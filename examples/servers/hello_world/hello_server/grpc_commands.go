package hello_world

import (
  "context"
  "log"
  pb "hello_world/glotos"
)

func (helloWorldServer *HelloServer) UnaryCallPlugin(CallContext context.Context, HelloWordServerRequest *pb.PluginUnaryRequest) (*pb.PluginUnaryResponse, error) {
  log.Println("Hello")
  log.Println(HelloWordServerRequest)

  return nil, nil
}
