from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRING: _ClassVar[InputType]
    INT: _ClassVar[InputType]
    FLOAT: _ClassVar[InputType]
    BOOL: _ClassVar[InputType]
STRING: InputType
INT: InputType
FLOAT: InputType
BOOL: InputType

class FunctionInput(_message.Message):
    __slots__ = ("Name", "Type", "Default", "InputHelp")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    INPUTHELP_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Type: InputType
    Default: str
    InputHelp: str
    def __init__(self, Name: _Optional[str] = ..., Type: _Optional[_Union[InputType, str]] = ..., Default: _Optional[str] = ..., InputHelp: _Optional[str] = ...) -> None: ...

class PluginCommand(_message.Message):
    __slots__ = ("CommandName", "FunctionInputDefs", "SubCommands", "CommandHelp")
    COMMANDNAME_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONINPUTDEFS_FIELD_NUMBER: _ClassVar[int]
    SUBCOMMANDS_FIELD_NUMBER: _ClassVar[int]
    COMMANDHELP_FIELD_NUMBER: _ClassVar[int]
    CommandName: str
    FunctionInputDefs: _containers.RepeatedCompositeFieldContainer[FunctionInput]
    SubCommands: _containers.RepeatedCompositeFieldContainer[PluginCommand]
    CommandHelp: str
    def __init__(self, CommandName: _Optional[str] = ..., FunctionInputDefs: _Optional[_Iterable[_Union[FunctionInput, _Mapping]]] = ..., SubCommands: _Optional[_Iterable[_Union[PluginCommand, _Mapping]]] = ..., CommandHelp: _Optional[str] = ...) -> None: ...

class PluginDefintion(_message.Message):
    __slots__ = ("PluginName", "PluginUUID", "PluginCommands", "Address", "BinaryLoc", "GitSha")
    PLUGINNAME_FIELD_NUMBER: _ClassVar[int]
    PLUGINUUID_FIELD_NUMBER: _ClassVar[int]
    PLUGINCOMMANDS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BINARYLOC_FIELD_NUMBER: _ClassVar[int]
    GITSHA_FIELD_NUMBER: _ClassVar[int]
    PluginName: str
    PluginUUID: int
    PluginCommands: _containers.RepeatedCompositeFieldContainer[PluginCommand]
    Address: str
    BinaryLoc: str
    GitSha: str
    def __init__(self, PluginName: _Optional[str] = ..., PluginUUID: _Optional[int] = ..., PluginCommands: _Optional[_Iterable[_Union[PluginCommand, _Mapping]]] = ..., Address: _Optional[str] = ..., BinaryLoc: _Optional[str] = ..., GitSha: _Optional[str] = ...) -> None: ...

class Manifest(_message.Message):
    __slots__ = ("Plugins",)
    class PluginsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PluginDefintion
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PluginDefintion, _Mapping]] = ...) -> None: ...
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    Plugins: _containers.MessageMap[str, PluginDefintion]
    def __init__(self, Plugins: _Optional[_Mapping[str, PluginDefintion]] = ...) -> None: ...

class PluginGetRequest(_message.Message):
    __slots__ = ("PluginName",)
    PLUGINNAME_FIELD_NUMBER: _ClassVar[int]
    PluginName: str
    def __init__(self, PluginName: _Optional[str] = ...) -> None: ...

class PluginGetResponse(_message.Message):
    __slots__ = ("PluginDef",)
    PLUGINDEF_FIELD_NUMBER: _ClassVar[int]
    PluginDef: PluginDefintion
    def __init__(self, PluginDef: _Optional[_Union[PluginDefintion, _Mapping]] = ...) -> None: ...

class PluginListResponse(_message.Message):
    __slots__ = ("PluginNames",)
    PLUGINNAMES_FIELD_NUMBER: _ClassVar[int]
    PluginNames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, PluginNames: _Optional[_Iterable[str]] = ...) -> None: ...

class PluginRegisterRequest(_message.Message):
    __slots__ = ("PluginServiceDefinition", "PluginName", "uuid")
    PLUGINSERVICEDEFINITION_FIELD_NUMBER: _ClassVar[int]
    PLUGINNAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    PluginServiceDefinition: PluginDefintion
    PluginName: str
    uuid: int
    def __init__(self, PluginServiceDefinition: _Optional[_Union[PluginDefintion, _Mapping]] = ..., PluginName: _Optional[str] = ..., uuid: _Optional[int] = ...) -> None: ...

class PluginRegisterResponse(_message.Message):
    __slots__ = ("ReponseCode", "ReponseString")
    REPONSECODE_FIELD_NUMBER: _ClassVar[int]
    REPONSESTRING_FIELD_NUMBER: _ClassVar[int]
    ReponseCode: int
    ReponseString: str
    def __init__(self, ReponseCode: _Optional[int] = ..., ReponseString: _Optional[str] = ...) -> None: ...

class PluginUnaryRequest(_message.Message):
    __slots__ = ("ClientCommandFile",)
    CLIENTCOMMANDFILE_FIELD_NUMBER: _ClassVar[int]
    ClientCommandFile: bytes
    def __init__(self, ClientCommandFile: _Optional[bytes] = ...) -> None: ...

class PluginUnaryResponse(_message.Message):
    __slots__ = ("ServerResponseFile",)
    SERVERRESPONSEFILE_FIELD_NUMBER: _ClassVar[int]
    ServerResponseFile: bytes
    def __init__(self, ServerResponseFile: _Optional[bytes] = ...) -> None: ...
