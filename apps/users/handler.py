import json

from tornado.web import RequestHandler


class SmsHandler(RequestHandler):
    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode('utf8')
        param = json.loads(param)
        pass
