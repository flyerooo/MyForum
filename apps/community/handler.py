import jwt
from tornado.web import authenticated
from MyForum.handler import RedisHandler
from apps.utils import AsyncYunPian
from apps.users.models import User
import functools

from apps.utils.forum_decorators import authenticated_async


class GroupHandler(RedisHandler):
    @authenticated_async
    async def post(self, *args, **kwargs):
        tsessionid = self.request.headers.get('tsessionid', None)
        if tsessionid:
            send_data = jwt.decode(tsessionid, 'abc', leeway=self.settings['jwt_expire'], optionns={'verify_exp': True})

        else:
            self.set_status(401)
        self.finish()

        self.request.headers.get('tsessionid', None)
        pass
