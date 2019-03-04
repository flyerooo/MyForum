import json
import requests

web_url = 'http://127.0.0.1:8888'


def test_sms():
    url = '{}/code/'.format(web_url)
    data = {
        'mobile': '18988888888'
    }
    res = requests.post(url, json=data)
    print(json.loads(res.text))


def test_register():
    url = '{}/register/'.format(web_url)
    data = {
        "mobile": "189888888881",
        "code": "00001",
        "password": "admin"
    }
    res = requests.post(url, json=data)
    # print(res.text)
    print(json.loads(res.text))


if __name__ == '__main__':
    # test_sms()
    test_register()
