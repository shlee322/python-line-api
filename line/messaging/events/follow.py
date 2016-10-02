from .event import ReplyEvent


class FollowEvent(ReplyEvent):
    type = 'follow'
