# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: glotos.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'glotos.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cglotos.proto\x1a\x1bgoogle/protobuf/empty.proto\"[\n\rFunctionInput\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x18\n\x04Type\x18\x02 \x01(\x0e\x32\n.InputType\x12\x0f\n\x07\x44\x65\x66\x61ult\x18\x03 \x01(\t\x12\x11\n\tInputHelp\x18\x04 \x01(\t\"\x9e\x01\n\rPluginCommand\x12\x13\n\x0b\x43ommandName\x18\x01 \x01(\t\x12)\n\x11\x46unctionInputDefs\x18\x02 \x03(\x0b\x32\x0e.FunctionInput\x12#\n\x0bSubCommands\x18\x03 \x03(\x0b\x32\x0e.PluginCommand\x12\x18\n\x0b\x43ommandHelp\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_CommandHelp\"\xb9\x01\n\x0fPluginDefintion\x12\x12\n\nPluginName\x18\x01 \x01(\t\x12\x12\n\nPluginUUID\x18\x02 \x01(\x03\x12&\n\x0ePluginCommands\x18\x03 \x03(\x0b\x32\x0e.PluginCommand\x12\x14\n\x07\x41\x64\x64ress\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tBinaryLoc\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x0e\n\x06GitSha\x18\x06 \x01(\tB\n\n\x08_AddressB\x0c\n\n_BinaryLoc\"u\n\x08Manifest\x12\'\n\x07Plugins\x18\x01 \x03(\x0b\x32\x16.Manifest.PluginsEntry\x1a@\n\x0cPluginsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.PluginDefintion:\x02\x38\x01\"&\n\x10PluginGetRequest\x12\x12\n\nPluginName\x18\x01 \x01(\t\"8\n\x11PluginGetResponse\x12#\n\tPluginDef\x18\x01 \x01(\x0b\x32\x10.PluginDefintion\")\n\x12PluginListResponse\x12\x13\n\x0bPluginNames\x18\x01 \x03(\t\"J\n\x15PluginRegisterRequest\x12\x31\n\x17PluginServiceDefinition\x18\x01 \x01(\x0b\x32\x10.PluginDefintion\"`\n\x16PluginRegisterResponse\x12\x13\n\x0bReponseCode\x18\x01 \x01(\x05\x12\x1a\n\x12PluginAssignedUUID\x18\x02 \x01(\x05\x12\x15\n\rReponseString\x18\x03 \x01(\t\"/\n\x12PluginUnaryRequest\x12\x19\n\x11\x43lientCommandFile\x18\x01 \x01(\x0c\"1\n\x13PluginUnaryResponse\x12\x1a\n\x12ServerResponseFile\x18\x01 \x01(\x0c*5\n\tInputType\x12\n\n\x06STRING\x10\x00\x12\x07\n\x03INT\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x32\xbd\x01\n\x08Registry\x12\x32\n\tGetPlugin\x12\x11.PluginGetRequest\x1a\x12.PluginGetResponse\x12\x41\n\x0eRegisterPlugin\x12\x16.PluginRegisterRequest\x1a\x17.PluginRegisterResponse\x12:\n\x0bListPlugins\x12\x16.google.protobuf.Empty\x1a\x13.PluginListResponse2F\n\x06Plugin\x12<\n\x0fUnaryCallPlugin\x12\x13.PluginUnaryRequest\x1a\x14.PluginUnaryResponseB5Z3/Users/isaak.willett/code/glopher/glogistery/protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'glotos_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3/Users/isaak.willett/code/glopher/glogistery/protos'
  _globals['_MANIFEST_PLUGINSENTRY']._loaded_options = None
  _globals['_MANIFEST_PLUGINSENTRY']._serialized_options = b'8\001'
  _globals['_INPUTTYPE']._serialized_start=1021
  _globals['_INPUTTYPE']._serialized_end=1074
  _globals['_FUNCTIONINPUT']._serialized_start=45
  _globals['_FUNCTIONINPUT']._serialized_end=136
  _globals['_PLUGINCOMMAND']._serialized_start=139
  _globals['_PLUGINCOMMAND']._serialized_end=297
  _globals['_PLUGINDEFINTION']._serialized_start=300
  _globals['_PLUGINDEFINTION']._serialized_end=485
  _globals['_MANIFEST']._serialized_start=487
  _globals['_MANIFEST']._serialized_end=604
  _globals['_MANIFEST_PLUGINSENTRY']._serialized_start=540
  _globals['_MANIFEST_PLUGINSENTRY']._serialized_end=604
  _globals['_PLUGINGETREQUEST']._serialized_start=606
  _globals['_PLUGINGETREQUEST']._serialized_end=644
  _globals['_PLUGINGETRESPONSE']._serialized_start=646
  _globals['_PLUGINGETRESPONSE']._serialized_end=702
  _globals['_PLUGINLISTRESPONSE']._serialized_start=704
  _globals['_PLUGINLISTRESPONSE']._serialized_end=745
  _globals['_PLUGINREGISTERREQUEST']._serialized_start=747
  _globals['_PLUGINREGISTERREQUEST']._serialized_end=821
  _globals['_PLUGINREGISTERRESPONSE']._serialized_start=823
  _globals['_PLUGINREGISTERRESPONSE']._serialized_end=919
  _globals['_PLUGINUNARYREQUEST']._serialized_start=921
  _globals['_PLUGINUNARYREQUEST']._serialized_end=968
  _globals['_PLUGINUNARYRESPONSE']._serialized_start=970
  _globals['_PLUGINUNARYRESPONSE']._serialized_end=1019
  _globals['_REGISTRY']._serialized_start=1077
  _globals['_REGISTRY']._serialized_end=1266
  _globals['_PLUGIN']._serialized_start=1268
  _globals['_PLUGIN']._serialized_end=1338
# @@protoc_insertion_point(module_scope)
