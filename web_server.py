"""A server-side Flask app to parse POST requests from GroupMe."""

import json
from json import loads
from multiprocessing import Process

import requests
from flask import Flask, request

from constants import WEBHOOK_URL


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    """Method for base route."""
    message_object = loads(request.data)
    """Prevents the bot from posting its own messages to Discord at all, rather than posting and immediately deleting them."""
    if message_object['name'] == 'your bots name in groupme':
        return ''
    data = {}
    data['username'] = message_object['name']
    data['content'] = message_object['text']
    data['avatar_url'] = message_object['avatar_url']
    attachment_url = ''
    attachment_is_image = False
    attachments = message_object['attachments']
    if len(attachments) > 0:
        print(attachments[0].items())
        if attachments[0]['type'] == 'image':
            attachment_is_image = True
           attachment_url = attachments[0]['url']
        
    data['embeds'] = []
    embed = {}
    if attachment_url:
        if attached_is_image:
            embed['image'] = {}
            embed['image']['url'] = attachment_url
        else:
            embed['title'] = message_object['name'],' uploaded a non-image attachment.'
            embed['url'] = attachment_url
        data['embeds'].append(embed)
        
    requests.post(
        WEBHOOK_URL, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    return ''


def main(*args, **kwargs):
    """Start the webserver with the provided options."""
    Process(target=app.run, args=args, kwargs=kwargs).start()
