import os

import click

CONFIG_STANDARDIZED_LOCATION = os.path.join(os.environ["HOME"], "glopher.config.yaml")
CONFIG_ENV_NAME = "GLOPHER_CONFIG_PATH"

config_option = click.option(
    '-cfg', '--config', "config", envvar=CONFIG_ENV_NAME, default=CONFIG_STANDARDIZED_LOCATION, type=str, help="EAI cli config file path.")

plugin_name_option = click.option(
    '-pgn', '--plugin_name', "plugin_name", type=str, help="Name of plugin")
