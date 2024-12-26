import logging
import time
import threading

import grpc
from grpc_health.v1 import health_pb2, health_pb2_grpc

from glopher.glotos.glotos_pb2 import PluginUnaryResponse, PluginUnaryRequest
from glopher.glotos.glotos_pb2_grpc import PluginStub
from glopher.general.threading import thread_handler


class PluginClient:

    def __init__(
        self,
        plugin_name: str,
        plugin_address: str
    ) -> None:
        logging.info(f"Creating GRPC connection to {plugin_name}.") 
        self.plugin_address = plugin_address
        self.plugin_name = plugin_name
        self.insecure_channel = grpc.insecure_channel(
            self.plugin_address
        )

        # setup health check background process
        threading.excepthook = thread_handler
        self._health_check_thread = threading.Thread(target=self._health_check)
        self._health_check_thread.daemon = True
        self._health_check_thread.start()

        self.stub = PluginStub(self.insecure_channel)
    
    def _health_check(self):
        healthy = True
        exception = Exception()
        while healthy:
            stub = health_pb2_grpc.HealthStub(self.insecure_channel)
            request = health_pb2.HealthCheckRequest(service=self.plugin_name)
            try:
                response = stub.Check(request)
                if response.status == health_pb2.HealthCheckResponse.SERVING:
                    logging.debug(f"Service {self.plugin_name} is healthy.")
                    time.sleep(60)
                else:
                    healthy = False
                    exception = grpc.RpcError(f"Service '{self.plugin_name}' is not healthy: {response.status}")
            except grpc.RpcError as e:
                healthy = False
                exception = grpc.RpcError(f"Error checking health: {e}")
        raise exception

    def unary_plugin_call(self, request_file_buffer: bytes) -> PluginUnaryResponse:
        # form the request buffer to a proto request
        unary_request = PluginUnaryRequest(ClientCommandFile=request_file_buffer)

        unary_response = self.stub.UnaryCallPlugin(unary_request)

        return unary_response
