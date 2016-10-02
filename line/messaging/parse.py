from .events import EVENT_CLASSES as __EVENT_CLASSES

EVENTS_DICT = {cls.type: cls for cls in __EVENT_CLASSES}


def event_parser(json, channel=None):
    from .events import UndefinedEvent

    event_cls = EVENTS_DICT.get(json.get('type'), UndefinedEvent)
    return event_cls(json=json, channel=channel)
