from .event import Event
from .beacon import BeaconEvent
from .follow import FollowEvent
from .join import JoinEvent
from .leave import LeaveEvent
from .message import MessageEvent
from .postback import PostbackEvent
from .unfollow import UnfollowEvent
from .undefined import UndefinedEvent


EVENT_CLASSES = [
    BeaconEvent,
    FollowEvent,
    JoinEvent,
    LeaveEvent,
    MessageEvent,
    PostbackEvent,
    UnfollowEvent,
    UndefinedEvent
]
