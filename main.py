"""Main entry point for running both server and bot."""

import web_server
import discord_bot
import time

from credentials import *


for instance in settings:
    GROUPME_ID = instance['bot_id']
    CHANNEL_NAME = instance['channel_name']
    WEBHOOK_URL = instance['webhook_url']
    LOCAL_PORT = instance['local_port']

    try:
        gm_token=instance['groupme_token']
    except KeyError:
        gm_token=GROUPME_TOKEN

    flask_options = {}

    if "false" not in str(LOCAL_PORT):
        flask_options = {'host': '127.0.0.1', 'port': LOCAL_PORT}

    discord_bot.main(BOT_TOKEN,  gm_token, GROUPME_ID, CHANNEL_NAME)
    web_server.main(WEBHOOK_URL, **flask_options)
    time.sleep(1)
