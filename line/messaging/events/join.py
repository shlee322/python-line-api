from .event import ReplyEvent


class JoinEvent(ReplyEvent):
    type = 'join'
