import os
import shellingham
import logging

import click

from glopher.config.types import Config
from glopher.registry.grpc import RegistryClient
from glopher.glotos.glotos_pb2 import Manifest
from glopher.host_module.manifest import install_plugin_to_manifest, uninstall_plugin_from_manifest


def init_cmd(config: Config) -> None:
    logging.info(f"Linking glopher to local cli name def, {config.cli_name}")
    shell_file = os.path.join(os.path.expanduser("~"), ".bashrc")
    shell, _ = shellingham.detect_shell()

    if shell == "zsh":
        shell_file = os.path.join(os.path.expanduser("~"), ".zshrc")

    with open(shell_file, "a") as open_shell_rc:
        open_shell_rc.write(f"alias {config.cli_name}=glopher\n")

def install_plugin_cmd(plugin_name: str, registry_address: str, manifest: Manifest, manifest_path: str) -> None:
    click.echo(f"Installing {plugin_name}")
    registry_client = RegistryClient(registry_address=registry_address)
    plugin_get_response = registry_client.get_plugin(plugin_name=plugin_name)
    install_plugin_to_manifest(
        manifest=manifest,
        manifest_path=manifest_path,
        plugin=plugin_get_response.PluginDef,
        plugin_name=plugin_name)
    click.echo(f"Installed {plugin_name}")

def uninstall_plugin_cmd(plugin_name: str, manifest: Manifest, manifest_path: str) -> None:
    click.echo(f"Uninstalling {plugin_name}")
    uninstall_plugin_from_manifest(
            manifest=manifest,
            manifest_path=manifest_path,
            plugin_name=plugin_name)
    click.echo(f"Uninstalled {plugin_name}")


def list_plugins_cmd(registry_address: str) -> None:
    registry_client = RegistryClient(registry_address=registry_address)
    available_plugin_list = registry_client.list_plugins()
    click.echo("Available Plugins:")
    for available_plugin in available_plugin_list.PluginNames:
        click.echo(f"- {available_plugin}")
