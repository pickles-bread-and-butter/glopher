package registry_server

import (
	"fmt"
	"github.com/spf13/viper"
	"google.golang.org/grpc"
	"google.golang.org/grpc/health"
	healthpb "google.golang.org/grpc/health/grpc_health_v1"
	"log"
	"net"

	pb "glogistery/glotos"
)

var (
	ConfigLocation = "glogistery_register_config.yaml"
)

type RegistryGRPCServer struct {
	pb.UnimplementedRegistryServer
}

func SetupRegistryServer() {
	LoadConfig()
	LoadManifest()
}

func SetupManifestWatcher() {
	go WatchManifest()
}

func StartRegistryServer() {
  lis, err := net.Listen("tcp", fmt.Sprintf("0.0.0.0:%d", viper.GetInt("AddressToServe")))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	RegistryGRPCServerInstance := RegistryGRPCServer{}
	pb.RegisterRegistryServer(s, &RegistryGRPCServerInstance)

	healthServer := health.NewServer()
	healthpb.RegisterHealthServer(s, healthServer)
	healthServer.SetServingStatus("Registry", healthpb.HealthCheckResponse_SERVING)

	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
