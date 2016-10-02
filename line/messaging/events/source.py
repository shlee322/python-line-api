class EventSource(object):
    type = None
    id = None

    def __init__(self, json, channel=None):
        self.json = json
        self.channel = channel

    def send_message(self, messages):
        self.channel.send_message(self, messages)


class User(EventSource):
    type = 'user'

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.id = self.json['userId']


class Group(EventSource):
    type = 'group'

    def __init__(self, *args, **kwargs):
        super(Group, self).__init__(*args, **kwargs)
        self.id = self.json['groupId']


class Room(EventSource):
    type = 'room'

    def __init__(self, *args, **kwargs):
        super(Room, self).__init__(*args, **kwargs)
        self.id = self.json['roomId']


class UndefinedSource(EventSource):
    pass


SOURCE_CLASSES = [User, Group, Room, UndefinedSource]
SOURCE_DICT = {cls.type: cls for cls in SOURCE_CLASSES}


def source_parser(json, channel=None):
    source_cls = SOURCE_DICT.get(json['type'], UndefinedSource)
    return source_cls(json=json, channel=channel)
