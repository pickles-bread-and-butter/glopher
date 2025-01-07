package hello_world

import (
  pb "hello_world/glotos"
  "context"
  "time"
  "log"
	"net"
  "google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc"
	"google.golang.org/grpc/health"
	healthpb "google.golang.org/grpc/health/grpc_health_v1"
)

type HelloServer struct {
  pb.UnimplementedPluginServer
}

type ExpectedContract struct {
  name string 
}

func ServerStartRoutine() {
  // Create client for registry and register self
  creds := insecure.NewCredentials()
  conn, err := grpc.NewClient("localhost:8000", grpc.WithTransportCredentials(creds))
  if err != nil {
    log.Fatal(err)
  }
  defer conn.Close()

  regCli := pb.NewRegistryClient(conn)
  var commandHelp string = "say hello"
  helloWorldCommands := []*pb.PluginCommand{
    {CommandName: "echo",
      FunctionInputDefs: []*pb.FunctionInput{
        {Name: "name",
          Type: 0,
          Default: "max",
          InputHelp: "your name",
        },
      },
      CommandHelp: &commandHelp,
    },
  }
  var address string = "localhost:8008"
  HelloWorldServiceDef := pb.PluginDefintion{
    PluginName: "hello_world",
    PluginUUID: 0,
    PluginCommands: helloWorldCommands,
    Address: &address,
    BinaryLoc: nil,
    GitSha: "",
  }
  req := &pb.PluginRegisterRequest{
    PluginServiceDefinition: &HelloWorldServiceDef,   
  }
  
  context, cancel := context.WithTimeout(context.Background(), 10*time.Second)
  resp, err := regCli.RegisterPlugin(context, req)
  defer cancel()
  log.Fatal(resp)
}

func StartHelloServer() {
  lis, err := net.Listen("tcp", "localhost:8008")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()

  pluginServer := HelloServer{}
  pb.RegisterPluginServer(s, &pluginServer)
	
  healthServer := health.NewServer()
	healthpb.RegisterHealthServer(s, healthServer)
	healthServer.SetServingStatus("Registry", healthpb.HealthCheckResponse_SERVING)
	
  log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
