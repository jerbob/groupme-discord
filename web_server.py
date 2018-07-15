"""A server-side Flask app to parse POST requests from GroupMe."""

from json import loads

import requests
from flask import Flask, request

from constants import WEBHOOK_URL


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    """Method for base route."""
    message_object = loads(request.data)
    requests.post(
        WEBHOOK_URL, data={
            'username': message_object['name'],
            'content': message_object['text'],
            'avatar_url': message_object['avatar_url']
        }
    )
