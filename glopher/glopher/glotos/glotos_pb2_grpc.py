# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import glopher.glotos.glotos_pb2 as glotos__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in glotos_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class RegistryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPlugin = channel.unary_unary(
                '/Registry/GetPlugin',
                request_serializer=glotos__pb2.PluginGetRequest.SerializeToString,
                response_deserializer=glotos__pb2.PluginGetResponse.FromString,
                _registered_method=True)
        self.RegisterPlugin = channel.unary_unary(
                '/Registry/RegisterPlugin',
                request_serializer=glotos__pb2.PluginRegisterRequest.SerializeToString,
                response_deserializer=glotos__pb2.PluginRegisterResponse.FromString,
                _registered_method=True)
        self.ListPlugins = channel.unary_unary(
                '/Registry/ListPlugins',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=glotos__pb2.PluginListResponse.FromString,
                _registered_method=True)


class RegistryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPlugin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterPlugin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPlugins(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegistryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPlugin': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlugin,
                    request_deserializer=glotos__pb2.PluginGetRequest.FromString,
                    response_serializer=glotos__pb2.PluginGetResponse.SerializeToString,
            ),
            'RegisterPlugin': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPlugin,
                    request_deserializer=glotos__pb2.PluginRegisterRequest.FromString,
                    response_serializer=glotos__pb2.PluginRegisterResponse.SerializeToString,
            ),
            'ListPlugins': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPlugins,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=glotos__pb2.PluginListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Registry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Registry', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Registry(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPlugin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Registry/GetPlugin',
            glotos__pb2.PluginGetRequest.SerializeToString,
            glotos__pb2.PluginGetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegisterPlugin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Registry/RegisterPlugin',
            glotos__pb2.PluginRegisterRequest.SerializeToString,
            glotos__pb2.PluginRegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListPlugins(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Registry/ListPlugins',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            glotos__pb2.PluginListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class PluginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UnaryCallPlugin = channel.unary_unary(
                '/Plugin/UnaryCallPlugin',
                request_serializer=glotos__pb2.PluginUnaryRequest.SerializeToString,
                response_deserializer=glotos__pb2.PluginUnaryResponse.FromString,
                _registered_method=True)


class PluginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UnaryCallPlugin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PluginServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UnaryCallPlugin': grpc.unary_unary_rpc_method_handler(
                    servicer.UnaryCallPlugin,
                    request_deserializer=glotos__pb2.PluginUnaryRequest.FromString,
                    response_serializer=glotos__pb2.PluginUnaryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Plugin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Plugin', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Plugin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UnaryCallPlugin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Plugin/UnaryCallPlugin',
            glotos__pb2.PluginUnaryRequest.SerializeToString,
            glotos__pb2.PluginUnaryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
