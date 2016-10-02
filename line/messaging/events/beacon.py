from .event import ReplyEvent


class Beacon(object):
    json = None
    type = None
    hwid = None

    def __init__(self, json):
        self.json = json
        self.type = self.json['type']
        self.hwid = self.json['hwid']


class BeaconEvent(ReplyEvent):
    type = 'beacon'

    def __init__(self, *args, **kwargs):
        super(BeaconEvent, self).__init__(*args, **kwargs)
        self.beacon = Beacon(json=self.json['beacon'])
