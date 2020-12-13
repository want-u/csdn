# -*- coding: utf-8 -*-
# @Author  : LuoXian
# @Date    : 2020/4/27 11:36
# Software : PyCharm
# version： Python 3.8
# @File    : csdn.py
import requests
import sys

url = 'https://me.csdn.net/api/LuckyDraw_v2/signIn'
headers = {
    'cookie': sys.argv[1],
    'origin': 'https://i.csdn.net',
    'referer': 'https://i.csdn.net/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
}
data = {
    'ip': '""',
    'platform': '"pc-my"',
    'product': '"pc"',
    'user_agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"',
    'username': '"qq_45473744"',
    'uuid': '"10_7201804910-1587953817362-908392"',
}
r = requests.post(url, data=data, headers=headers)
print(r.text, r)
