from line.messaging import Channel

webhook = Channel(
    channel_secret='test',
    channel_access_token=None
).get_webhook()


@webhook.event_handler
def test_handler(event):
    pass


app = webhook.get_wsgi_application()


def test_request(obj):
    import json
    from webob import Request

    json_data = json.dumps({
        'events': [obj]
    })
    Request.blank('/', headers={
        'X-Line-Signature': ''
    }, POST=json_data).get_response(app)


test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "message",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    },
    "message": {
        "id": "325708",
        "type": "text",
        "text": "Hello, world"
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "message",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    },
    "message": {
        "id": "325708",
        "type": "image"
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "message",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    },
    "message": {
        "id": "325708",
        "type": "video"
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "message",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    },
    "message": {
        "id": "325708",
        "type": "audio"
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "message",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    },
    "message": {
        "id": "325708",
        "type": "location",
        "title": "my location",
        "address": "〒150-0002 東京都渋谷区渋谷２丁目２１−１",
        "latitude": 35.65910807942215,
        "longitude": 139.70372892916203
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "message",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    },
    "message": {
        "id": "325708",
        "type": "sticker",
        "packageId": "1",
        "stickerId": "1"
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "follow",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    }
})

test_request({
    "type": "unfollow",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "join",
    "timestamp": 1462629479859,
    "source": {
        "type": "group",
        "groupId": "cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
})

test_request({
    "type": "leave",
    "timestamp": 1462629479859,
    "source": {
        "type": "group",
        "groupId": "cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "postback",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    },
    "postback": {
        "data": "action=buyItem&itemId=123123&color=red"
    }
})

test_request({
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "type": "beacon",
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U206d25c2ea6bd87c17655609a1c37cb8"
    },
    "beacon": {
        "hwid": "d41d8cd98f",
        "type": "enter"
    }
})
