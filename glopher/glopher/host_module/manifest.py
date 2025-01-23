import yaml
import os
import logging

from google.protobuf.json_format import ParseDict, MessageToDict

from glopher.glotos.glotos_pb2 import Manifest, PluginDefintion


def unmarshall_manifest_from_yaml(manifest_path: str) -> Manifest:
    # expand user if required
    if manifest_path.startswith("~/"):
        manifest_path = manifest_path.replace("~", os.path.expanduser("~"))
    
    if not os.path.exists(manifest_path):
        logging.info(f"No manifest at {manifest_path}, creating blank manifest")
        open(manifest_path, "w+")

    with open(manifest_path, "r") as open_manifest_buffer:
        manifest_obj = yaml.safe_load(open_manifest_buffer)
        manifest_proto = Manifest()
        if manifest_obj:
            ParseDict(manifest_obj, manifest_proto)
    return manifest_proto


def add_to_manifest_object(manifest: Manifest, plugin: PluginDefintion, plugin_name: str) -> None:
    # add the plugin definition to manifest object
    plugins_in_manifest = manifest.Plugins
    if plugin_name in plugins_in_manifest:
        logging.warning(f"Overwriting {plugin_name} in manifest")
    new_manifest = Manifest(Plugins={plugin_name: plugin})
    manifest.MergeFrom(new_manifest)


def remove_from_manifest_obj(manifest: Manifest, plugin_name: str) -> None:
    if plugin_name not in manifest.Plugins:
        logging.warning(f"{plugin_name} not installed, see 'eai-cli --help' for list of active plugins.")
        return
    del manifest.Plugins[plugin_name]


def marshall_manifest_to_yaml(manifest_path: str, manifest: Manifest) -> None:
    # expand user if required
    if manifest_path.startswith("~/"):
        manifest_path = manifest_path.replace("~", os.path.expanduser("~"))
    
    if os.path.exists(manifest_path):
        logging.warning(f"Re-writing manifest at {manifest_path}")

    with open(manifest_path, "w") as open_manifest_buffer:
        manifest_dict = MessageToDict(manifest)
        yaml.dump(manifest_dict, open_manifest_buffer)
    logging.info("Manifest updated.")
    

def install_plugin_to_manifest(manifest_path: str, manifest: Manifest, plugin: PluginDefintion, plugin_name: str) -> None:
    add_to_manifest_object(manifest=manifest, plugin=plugin, plugin_name=plugin_name)
    marshall_manifest_to_yaml(manifest=manifest, manifest_path=manifest_path)

def uninstall_plugin_from_manifest(manifest_path: str, manifest: Manifest, plugin_name: str) -> None:
    remove_from_manifest_obj(manifest=manifest, plugin_name=plugin_name)
    marshall_manifest_to_yaml(manifest=manifest, manifest_path=manifest_path)
