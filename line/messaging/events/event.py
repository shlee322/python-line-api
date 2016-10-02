

class Event(object):
    json = None
    timestamp = None
    type = None
    source = None

    def __init__(self, json=None, channel=None):
        self.json = json
        self.channel = channel

        from datetime import datetime
        self.timestamp = datetime.utcfromtimestamp(self.json['timestamp'] / 1000)

        from line.messaging.events.source import source_parser
        self.source = source_parser(json=self.json['source'], channel=self.channel)


class ReplyEvent(Event):
    reply_token = None

    def __init__(self, *args, **kwargs):
        super(ReplyEvent, self).__init__(*args, **kwargs)
        self.reply_token = self.json['replyToken']

    def reply(self, messages):
        self.channel.reply(self.reply_token, messages)
