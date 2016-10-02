# python-line-api

SDK of the LINE Messaging API for Python.

## Getting Started
```python
from line.messaging import Channel
from line.messaging.events import MessageEvent
from line.messaging.message import TextMessage

webhook = Channel(
    channel_secret='your channel secret',
    channel_access_token='your channel access token'
).get_webhook()

@webhook.event_handler
def test_handler(event):
    if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
        event.reply(event.message)
        event.source.send_message(TextMessage(message='test'))

webhook.run(certfile='./test.cert', keyfile='./test.key')
```

## About LINE Messaging API

Please refer to the official api documents for details.

https://devdocs.line.me/en/

## Installation
```sh
pip install line-api
```

## LICENSE

See LICENSE.txt

## Note. Get SSL Certificate (letsencrypt)
```sh
sudo apt-get install letsencrypt
letsencrypt certonly --standalone -d (your webhook domain)
```
