"""Parse constants from the config file and environment variables."""

from os import environ
from typing import Union
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')


def get_constant(
    env_name: str, config_header: str, config_key: str
) -> Union[str, int]:
    """Get a constant from the environment or config."""
    constant = environ.get(env_name) or config.get(config_header, config_key)
    if constant.isnumeric():
        constant = int(constant)
    return constant


RUN_LOCAL = config.getboolean('flask', 'run_locally')
GROUPME_ID = get_constant('GROUPME_ID', 'groupme', 'bot_id')
BOT_TOKEN = get_constant('DISCORD_BOT_TOKEN', 'discord', 'bot_token')
WEBHOOK_URL = get_constant('DISCORD_WEBHOOK', 'discord', 'webhook_url')
GROUPME_TOKEN = get_constant('GROUPME_TOKEN', 'groupme', 'access_token')
CHANNEL_ID = get_constant('DISCORD_CHANNEL_ID', 'discord', 'channel_id')
