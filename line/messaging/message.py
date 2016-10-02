
class Message(object):
    json = None
    id = None
    type = None
    channel = None

    def __init__(self, json, channel=None):
        self.json = json
        self.channel = channel
        self.id = self.json['id'] if self.json else None

    def send(self, to):
        self.channel.send_message(to, [self])

    def get_json(self):
        raise NotImplementedError()


class TextMessage(Message):
    type = 'text'
    text = None

    def __init__(self, json=None, message=None, *args, **kwargs):
        super(TextMessage, self).__init__(json=json, *args, **kwargs)
        self.text = message if message else self.json['text']

    def get_json(self):
        return {
            'type': 'text',
            'text': self.text
        }


class ContentMessage(Message):
    def get_content(self):
        return self.channel.get_content(self.id)


class ImageMessage(ContentMessage):
    type = 'image'
    original_content_url = None
    preview_image_url = None

    def __init__(self, original_content_url=None, preview_image_url=None, *args, **kwargs):
        super(ImageMessage, self).__init__(*args, **kwargs)
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class VideoMessage(ContentMessage):
    type = 'video'
    original_content_url = None
    preview_image_url = None

    def __init__(self, original_content_url=None, preview_image_url=None, *args, **kwargs):
        super(VideoMessage, self).__init__(*args, **kwargs)
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class AudioMessage(ContentMessage):
    type = 'audio'
    original_content_url = None
    duration = None

    def __init__(self, original_content_url=None, duration=None, *args, **kwargs):
        super(AudioMessage, self).__init__(*args, **kwargs)
        self.original_content_url = original_content_url
        self.duration = duration


class LocationMessage(Message):
    type = 'location'
    title = None
    address = None
    latitude = None
    longitude = None

    def __init__(self, *args, **kwargs):
        super(LocationMessage, self).__init__(*args, **kwargs)
        self.title = self.json['title']
        self.address = self.json['address']
        self.latitude = self.json['latitude']
        self.longitude = self.json['longitude']


class StickerMessage(Message):
    type = 'sticker'
    package_id = None
    sticker_id = None

    def __init__(self, *args, **kwargs):
        super(StickerMessage, self).__init__(*args, **kwargs)
        self.package_id = self.json['packageId']
        self.sticker_id = self.json['stickerId']


class UndefinedMessage(Message):
    pass


class ImagemapMessage(Message):
    pass


class ButtonsMessage(Message):
    pass


class ConfirmMessage(Message):
    pass


class CarouselMessage(Message):
    pass


MESSAGE_CLASSES = [
    TextMessage, ContentMessage, ImageMessage,
    VideoMessage, AudioMessage, LocationMessage,
    StickerMessage, UndefinedMessage
]
MESSAGE_DICT = {cls.type: cls for cls in MESSAGE_CLASSES}
