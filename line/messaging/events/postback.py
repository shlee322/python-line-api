from .event import ReplyEvent


class Postback(object):
    json = None
    data = None

    def __init__(self, json):
        self.json = json
        self.data = self.json['data']


class PostbackEvent(ReplyEvent):
    type = 'postback'
    postback = None

    def __init__(self, *args, **kwargs):
        super(PostbackEvent, self).__init__(*args, **kwargs)
        self.postback = Postback(json=self.json['postback'])
