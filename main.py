"""Main entry point for running both server and bot."""

import web_server
import discord_bot

from constants import RUN_LOCAL


flask_options = {}

if not RUN_LOCAL:
    flask_options = {'host': '0.0.0.0'}

discord_bot.main()
web_server.main(**flask_options)
