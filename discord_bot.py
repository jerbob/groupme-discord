"""Discord-side message parsing and posting to GroupMe."""

import json
from os import path
from io import BytesIO
from random import randint
from typing import List, Union, Optional, Callable

from discord.ext import commands
from aiohttp import ClientSession
from discord import Attachment, Message

from constants import BOT_TOKEN, GROUPME_TOKEN, GROUPME_ID, CHANNEL_ID


async def post(
    session: ClientSession, url: str,
    payload: Union[BytesIO, dict], headers: Optional[dict] = None
) -> str:
    """Post data to a specified url."""
    async with session.post(url, data=payload) as response:
        return await response.text()


def get_prefix(
    bot_instance: commands.Bot, message: Message
) -> Callable[[commands.Bot, Message], list]:
    """Decide prefixes of the Bot."""
    prefixes = ['chat!', '>']
    return commands.when_mentioned_or(*prefixes)(bot_instance, message)


bot = commands.Bot(command_prefix=get_prefix)
endpoint = f'https://api.groupme.com/v3/bots/post'

sent_buffer = []  # Buffer for webhook message deletions.


async def send_message(message: Message) -> str:
    """Send a message to the group chat."""
    text = f'{message.author.display_name}: {message.content}'.strip()
    sent_buffer.append(text)
    if len(sent_buffer) > 10:
        sent_buffer.pop(0)
    payload = {
        'bot_id': GROUPME_ID,
        'text': f'{message.author.display_name}: {message.content}'
    }
    cdn = await process_attachments(message.attachments)
    if cdn is not None:
        payload.update({'picture_url': cdn})
    async with ClientSession() as session:
        return await post(session, endpoint, payload)


async def process_attachments(attachments: List[Attachment]) -> str:
    """Process the attachments of a message and return GroupMe objects."""
    if not attachments:
        return
    attachment = attachments[0]
    url = 'https://image.groupme.com/pictures'
    if not attachment.filename.endswith(('jpeg', 'jpg', 'png')):
        return
    extension = attachment.filename.partition('.')[-1]
    if extension == 'jpg':
        extension = 'jpeg'
    handler = BytesIO()
    await attachment.save(handler)
    headers = {
        'X-Access-Token': GROUPME_TOKEN,
        'Content-Type': f'image/{extension}'
    }
    async with ClientSession(headers=headers) as session:
        cdn = await post(session, url, handler.read())
        cdn = json.loads(cdn)['payload']['url']
    return cdn


@bot.event
async def on_ready() -> None:
    """Called when the bot loads."""
    print('-------------\nBot is ready!\n-------------')


@bot.event
async def on_message(message: Message) -> None:
    """Called on each message sent in a channel."""
    if message.channel.id == CHANNEL_ID:
        if not message.author.bot:
            print(await send_message(message))
        elif message.content in sent_buffer:
            await message.delete()


if __name__ == '__main__':
    bot.run(BOT_TOKEN)
