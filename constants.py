"""Parse constants from the config file and environment variables."""

from os import environ
from typing import Union


def get_constant(
    env_name: str, config_header: str, config_key: str
) -> Union[str, int]:
    """Get a constant from the environment or config."""
    constant = environ.get(env_name) 
    if constant.isnumeric():
        constant = int(constant)
    return constant


BOT_TOKEN = get_constant('DISCORD_BOT_TOKEN', 'discord', 'bot_token')
GROUPME_TOKEN = get_constant('GROUPME_TOKEN', 'groupme', 'access_token')