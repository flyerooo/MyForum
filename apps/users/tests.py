import json
import requests

web_url = 'http://127.0.0.1:8888'

temp_url = 'http://59.41.223.227:8082/face-manage/api/login'


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


def temp_login():
    data = {
        'username': 'lxc',
        'password': '123'
    }
    res = requests.post(temp_url, json=data)
    print(json.loads(res.text))


from collections import OrderedDict


def count_dict(data):
    num_count = {}
    for num in data:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count.update({num: 1})
    return OrderedDict(sorted(num_count.items()))

def median_index(size):
    return size / 2 if size % 2 == 0 else (size - 1) / 2

def median(sorted_dict, media_index):
    sum = 0
    for key, value in sorted_dict.items():
        sum += value
        if sum >= media_index:
            return key

if __name__ == '__main__':
    import random
    import time

    # 测试
    start_time = time.time()
    big_data = (random.randint(10 ** 31, 10 ** 32 - 1) for _ in range(10 ** 7))
    sorted_dict = count_dict(big_data)
    size = sum(sorted_dict.values())
    median_index = median_index(size)
    median = median(sorted_dict, median_index)
    print(median)
    print(time.time()-start_time)

