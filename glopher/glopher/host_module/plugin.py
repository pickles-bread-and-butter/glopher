import click
import yaml
from typing import Any, Dict, List, Optional

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer

from glopher.glotos.glotos_pb2 import Manifest, PluginCommand, PluginDefintion, FunctionInput
from glopher.host_module.grpc import PluginClient


pytype_mapping = {
    0: str,
    1: int,
    2: float,
    3: bool
}


def form_plugins(head_command: click.core.Group, manifest: Manifest):
    installed_plugins = manifest.Plugins
    for plugin_name, plugin_definition in installed_plugins.items():
        plugin_command = form_generic_plugin(plugin_name=plugin_name, plugin_definition=plugin_definition)
        
        head_command.add_command(plugin_command)


def form_options_from_function_input_defs(function_input_defs: Optional[RepeatedCompositeFieldContainer[FunctionInput]]):
    def decorator(f: Any) -> Any:
        if function_input_defs:
            for function_input_def in function_input_defs:
                default_value = pytype_mapping[function_input_def.Type](function_input_def.Default)
                click.option(
                f"--{function_input_def.Name}", function_input_def.Name, type=pytype_mapping[function_input_def.Type],
                default=default_value, help=function_input_def.InputHelp)(f)
        return f
    return decorator


def form_generic_plugin(plugin_name: str, plugin_definition: PluginDefintion) -> click.core.Command:
    @click.group(name=plugin_definition.PluginName, help=f"Plugin command grouping for {plugin_definition.PluginName}")
    @click.pass_context
    def generic_plugin_command(_: click.Context) -> None:
        pass
    plugin_commands = form_generic_commands(command_definitions=plugin_definition.PluginCommands, plugin_address=plugin_definition.Address, plugin_name=plugin_name)
    for plugin_command in plugin_commands:
        generic_plugin_command.add_command(plugin_command)
    return generic_plugin_command


def form_generic_commands(command_definitions: RepeatedCompositeFieldContainer[PluginCommand], plugin_address: str, plugin_name: str):
    generic_commands = []
    for command_definition in command_definitions:
        if command_definition.SubCommands is not None:
            command_header = click.group(name=command_definition.CommandName, help=command_definition.CommandHelp)
            function = lambda kwargs, plugin_address, plugin_name: group_function()
        else:
            function = lambda kwargs, plugin_address, plugin_name: command_function(function_inputs=kwargs, plugin_address=plugin_address, plugin_name=plugin_name)
            command_header = click.command(name=command_definition.CommandName, help=command_definition.CommandHelp)
        
        @command_header
        @form_options_from_function_input_defs(function_input_defs=command_definition.FunctionInputDefs)
        @click.pass_context
        def generic_command(ctx: click.Context, **kwargs) -> None:
            function(kwargs=kwargs, plugin_address=plugin_address, plugin_name=plugin_name)

        if command_definition.SubCommands is not None and isinstance(generic_command, click.core.Group):
            sub_commands = form_generic_commands(command_definitions=command_definition.SubCommands, plugin_address=plugin_address, plugin_name=plugin_name)
            for sub_command in sub_commands:
                generic_command.add_command(sub_command)

        generic_commands.append(generic_command)

    return generic_commands


def group_function() -> None:
    pass


def command_function(function_inputs: Dict[str, Any], plugin_address: str,  plugin_name: str) -> None:
    # form the client first and let it check the connection that was given
    plugin_client = PluginClient(plugin_address=plugin_address, plugin_name=plugin_name)

    # Simply pack the dict into a yaml object and use that as the buffer for the message
    yaml_buffer = yaml.dump(function_inputs).encode("utf-8")

    # Send request to the plugin service and have it handle the logic
    plugin_response = plugin_client.unary_plugin_call(yaml_buffer)
