"""Main entry point for running both server and bot."""

import web_server
import discord_bot

from constants import *


flask_options = {}

if "false" now in LOCAL_PORT:
    flask_options = {'host': '0.0.0.0',port=LOCAL_PORT}

discord_bot.main(BOT_TOKEN, GROUPME_TOKEN, GROUPME_ID, CHANNEL_NAME)
web_server.main(WEBHOOK_URL,**flask_options)
