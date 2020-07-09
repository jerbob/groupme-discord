"""Main entry point for running both server and bot."""

import web_server
import discord_bot

from constants import RUN_LOCAL


flask_options = {}

if LOCAL_PORT:
    flask_options = {'host': '0.0.0.0',port=LOCAL_PORT}

discord_bot.main()
web_server.main(**flask_options)
