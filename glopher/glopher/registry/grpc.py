import logging
import time
import threading

import grpc
from google.protobuf import empty_pb2
from grpc_health.v1 import health_pb2, health_pb2_grpc

from glopher.glotos import glotos_pb2_grpc, glotos_pb2
from glopher.general.threading import thread_handler


REGISTRY_SERVICE_NAME = "Registry"


class RegistryClient:

    def __init__(
        self,
        registry_address: str
    ):
        logging.info("Creating GRPC connection to registry.") 
        self.registry_address = registry_address
        self.insecure_channel = grpc.insecure_channel(
            self.registry_address,
        )

        # setup health check background process
        threading.excepthook = thread_handler
        self._health_check_thread = threading.Thread(target=self._health_check)
        self._health_check_thread.daemon = True
        self._health_check_thread.start()

        # generate client as internal stub, recheck the connection after subsequent calls
        self.stub = glotos_pb2_grpc.RegistryStub(self.insecure_channel)

    def _health_check(self):
        healthy = True
        exception = Exception()
        while healthy:
            stub = health_pb2_grpc.HealthStub(self.insecure_channel)
            request = health_pb2.HealthCheckRequest(service=REGISTRY_SERVICE_NAME)
            try:
                response = stub.Check(request)
                if response.status == health_pb2.HealthCheckResponse.SERVING:
                    logging.debug(f"Service {REGISTRY_SERVICE_NAME} is healthy.")
                    time.sleep(60)
                else:
                    healthy = False
                    exception = grpc.RpcError(f"Service '{REGISTRY_SERVICE_NAME}' is not healthy: {response.status}")
            except grpc.RpcError as e:
                healthy = False
                exception = grpc.RpcError(f"Error checking health: {e}")
        raise exception

    def get_plugin(self, plugin_name: str) -> glotos_pb2.PluginGetResponse:
        get_plugin_request = glotos_pb2.PluginGetRequest(PluginName=plugin_name)
        get_plugin_response = self.stub.GetPlugin(get_plugin_request)
        return get_plugin_response
    
    def list_plugins(self) -> glotos_pb2.PluginListResponse:
        list_plugin_request = empty_pb2.Empty()
        list_plugin_response = self.stub.ListPlugins(list_plugin_request)
        return list_plugin_response
