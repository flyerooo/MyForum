import functools
import urllib.parse as urlparse
from urllib.parse import urlencode

from tornado.httpclient import HTTPError
import jwt

from apps.users.models import User


def authenticated_async(method):
    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs):
        tsessionid = self.request.headers.get('tsessionid', None)
        if tsessionid:
            try:
                send_data = jwt.decode(tsessionid, self.settings['secret_key'], leeway=1, optionns={'verify_exp': True})
                user_id = send_data['id']

                # 从数据库中获取user比你那个设置给_current_user
                try:
                    user = await self.application.objects.get(User, id=user_id)
                    self._current_user = user
                    await method(self, *args, **kwargs)
                except User.DoesNotExist as e:
                    self.set_status(401)
            except jwt.ExpiredSignatureError as e:
                self.set_status(401)
        else:
            self.set_status(401)
        self.finish()

    return wrapper
