

class Channel(object):
    channel_secret = None
    channel_access_token = None

    def __init__(self, channel_secret, channel_access_token):
        self.channel_secret = channel_secret
        self.channel_access_token = channel_access_token

    def get_webhook(self):
        from .webhook import Webhook
        return Webhook(channel=self)

    def get_content(self, content_id):
        import requests
        res = requests.get('https://api.line.me/v2/bot/message/%s/content' % content_id, headers={
            'Authorization': 'Bearer %s' % self.channel_access_token
        })
        return res

    def get_profile(self, user_id):
        import requests
        res = requests.get('https://api.line.me/v2/bot/profile/%s' % user_id, headers={
            'Authorization': 'Bearer %s' % self.channel_access_token
        })
        return res.json()

    def leave(self, type, id):
        import requests
        res = requests.post('https://api.line.me/v2/bot/%s/%s/leave' % (type, id), headers={
            'Authorization': 'Bearer %s' % self.channel_access_token
        })
        return res

    def reply(self, reply_token, messages):
        messages = messages if type(messages) is list else [messages]

        import requests
        res = requests.post('https://api.line.me/v2/bot/message/reply', headers={
            'Authorization': 'Bearer %s' % self.channel_access_token
        }, json={
            'replyToken': reply_token,
            'messages': [message.get_json() for message in messages]
        })
        return res

    def send_message(self, to, messages):
        messages = messages if type(messages) is list else [messages]

        import requests
        res = requests.post('https://api.line.me/v2/bot/message/push', headers={
            'Authorization': 'Bearer %s' % self.channel_access_token
        }, json={
            'to': to.id,
            'messages': [message.get_json() for message in messages]
        })
        return res
