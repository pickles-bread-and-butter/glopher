import yaml

from glopher.config.types import Config

def load_config(config_location: str) -> Config:
    with open(config_location, "r") as open_config_buffer:
        config_json = yaml.safe_load(open_config_buffer)
        config_dataclass = Config(**config_json) if config_json is not None else Config()

    return config_dataclass
    
