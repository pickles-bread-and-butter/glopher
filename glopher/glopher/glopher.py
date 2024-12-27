import os

import click
import pkg_resources

from glopher.registry.commands import init_cmd, install_plugin_cmd, uninstall_plugin_cmd, list_plugins_cmd
from glopher.config.config import load_config
from glopher.general.options import config_option, plugin_name_option, CONFIG_ENV_NAME, CONFIG_STANDARDIZED_LOCATION
from glopher.host_module.manifest import unmarshall_manifest_from_yaml
from glopher.host_module.plugin import form_plugins


@click.group(help="CLI interface to EAI services.")
@click.version_option(version=pkg_resources.get_distribution("glopher").version, prog_name="glopher")
@config_option
@click.pass_context
def glopher(ctx: click.Context, config: str) -> None:
    """EAI Vertex CLI"""
    config_obj = load_config(config)
    manifest_obj = unmarshall_manifest_from_yaml(config_obj.manifest_file_location)
    ctx.obj = {"config": config_obj, "manifest": manifest_obj}


@glopher.command(help="Init tool to link to custom naming")
@click.pass_context
def init(ctx: click.Context) -> None:
    init_cmd(config=ctx.obj.get("config"))

@glopher.command(help="Install plugin from registry")
@plugin_name_option
@click.pass_context
def install(ctx: click.Context, plugin_name: str) -> None:
    config_obj = ctx.obj["config"]
    manifest = ctx.obj["manifest"]
    install_plugin_cmd(
        plugin_name=plugin_name,
        registry_address=config_obj.registry_address,
        manifest_path=config_obj.manifest_file_location,
        manifest=manifest)


@glopher.command(help="Uninstall plugin from local")
@plugin_name_option
@click.pass_context
def uninstall(ctx: click.Context, plugin_name: str) -> None:
    config_obj = ctx.obj["config"]
    manifest = ctx.obj["manifest"]
    uninstall_plugin_cmd(
        plugin_name=plugin_name,
        manifest_path=config_obj.manifest_file_location,
        manifest=manifest
    )


@glopher.command(help="List available plugins in registry")
@click.pass_context
def list(ctx: click.Context) -> None:
    config_obj = ctx.obj["config"]
    list_plugins_cmd(config_obj.registry_address)


def main():
    config_obj = load_config(os.environ.get(CONFIG_ENV_NAME, CONFIG_STANDARDIZED_LOCATION))
    manifest_obj = unmarshall_manifest_from_yaml(config_obj.manifest_file_location)
    form_plugins(glopher, manifest_obj)
    glopher.name = config_obj.cli_name
    glopher()  # type: ignore
