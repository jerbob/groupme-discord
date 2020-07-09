"""Main entry point for running both server and bot."""

import web_server
import discord_bot

from constants import BOT_TOKEN, GROUPME_TOKEN #set as environment variables

settings = [
     {
        'bot_id': "60d8f6e70e5fe17ff5e236e072", #groupme
        'channel_name': "cs_memes", #discord
        'webhook_url': "https://discordapp.com/api/webhooks/730924768769081457/wB3rLeUJKnUrfk4clQaaYJ2eVHGm6WhJa2lLICSerHvBl4fYFmYhShaligTWknbK-h88",
        'local_port': 50070 #server
    }
]
for instance in settings:

    GROUPME_ID=instance['bot_id']
    CHANNEL_NAME=instance['channel_name']
    WEBHOOK_URL=instance['webhook_url']
    LOCAL_PORT=instance['local_port']

    flask_options = {}

    if "false" in str(LOCAL_PORT):
        flask_options = {'host': '0.0.0.0', port: LOCAL_PORT}

    discord_bot.main(BOT_TOKEN, GROUPME_TOKEN, GROUPME_ID, CHANNEL_NAME)
    web_server.main(WEBHOOK_URL, **flask_options)
