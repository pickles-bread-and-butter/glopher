import click

from glopher.registry.grpc import RegistryClient 
from glopher.glotos.glotos_pb2 import Manifest
from glopher.host_module.manifest import install_plugin_to_manifest, uninstall_plugin_from_manifest


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
