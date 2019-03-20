import json
import requests

from datetime import datetime

import jwt

from MyForum.settings import settings

curret_time = datetime.utcnow()


data = jwt.encode({
    'name':'jeff',
    'id':1,
    'exp':curret_time
}, settings['secret_key']).decode('utf8')

groups_url = 'http://127.0.0.1:8888/groups/'

res = requests.get(groups_url, headers={
    'tsessionid':data,

})

print(res.content)