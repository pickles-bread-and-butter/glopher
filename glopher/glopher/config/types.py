from dataclasses import dataclass

@dataclass
class Config:
    """EAI CLI config file, registry pointers and other things"""
    cli_name: str = "glopher"
    manifest_file_location: str = "~/.eai-plugin-manifest.yaml"
    registry_address: str = "localhost:50051"
