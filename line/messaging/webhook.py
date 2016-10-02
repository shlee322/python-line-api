

class Webhook(object):
    channel = None
    handler = None

    def __init__(self, channel):
        self.channel = channel

    def event_handler(self, func):
        self.handler = func
        return func

    def is_valid_sign(self, data, sign):
        import hmac
        import hashlib
        import base64
        sign_data = hmac.new(self.channel.channel_secret.encode(), msg=data, digestmod=hashlib.sha256).digest()
        return base64.b64encode(sign_data).decode() == sign

    def get_wsgi_application(self):
        def create_response(environ, start_response, status=200):
            from webob import Response
            res = Response(
                content_type='application/json',
                body='{}',
                status=status
            )
            return res(environ, start_response)

        def application(environ, start_response):
            import json
            from webob import Request
            request = Request(environ)

            # Check HMAC-SHA256
            if not self.is_valid_sign(request.body, request.headers.get('X-Line-Signature')):
                return create_response(environ, start_response, 403)

            # Check Handler
            if not self.handler:
                return create_response(environ, start_response, 501)

            # Parse Event
            try:
                obj = json.loads(request.body.decode('utf-8'))
                from .parse import event_parser
                events = [event_parser(event_json, self.channel) for event_json in obj['events']]
            except:
                return create_response(environ, start_response, 400)

            # Call Event Handler
            for event in events:
                self.handler(event)

            return create_response(environ, start_response)

        return application

    def run(self, port=8000, host='', certfile=None, keyfile=None):
        import ssl
        from wsgiref.simple_server import make_server
        httpd = make_server(host, port, self.get_wsgi_application())

        if certfile and keyfile:
            httpd.socket = ssl.wrap_socket(
                httpd.socket,
                certfile=certfile,
                keyfile=keyfile,
                server_side=True
            )

        print("Serving on port %s:%d..." % (host, port))
        httpd.serve_forever()
