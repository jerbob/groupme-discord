"""Main entry point for running both server and bot."""

from multiprocessing import Process

from web_server import app
from discord_bot import bot

from constants import BOT_TOKEN, RUN_LOCAL


flask_options = {'debug': True}

if not RUN_LOCAL:
    flask_options.update({'host': '0.0.0.0'})


Process(target=bot.run, args=(BOT_TOKEN,)).start()
Process(target=app.run, kwargs=flask_options).start()
