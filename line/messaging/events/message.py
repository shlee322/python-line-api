from .event import ReplyEvent
from ..message import MESSAGE_DICT, UndefinedMessage


class MessageEvent(ReplyEvent):
    type = 'message'
    message = None

    def __init__(self, *args, **kwargs):
        super(MessageEvent, self).__init__(*args, **kwargs)
        message_cls = MESSAGE_DICT.get(self.json['message']['type'], UndefinedMessage)
        self.message = message_cls(json=self.json['message'], channel=self.channel)
