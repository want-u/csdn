# -*- coding: utf-8 -*-
# @Author  : LuoXian
# @Date    : 2020/4/27 11:36
# Software : PyCharm
# version： Python 3.8
# @File    : csdn.py
import requests

url = 'https://me.csdn.net/api/LuckyDraw_v2/signIn'
headers = {
    'cookie': 'uuid_tt_dd=10_7201804910-1587953817362-908392; dc_session_id=10_1587953817362.493453; c_first_ref=www.baidu.com; c_first_page=https%3A//blog.csdn.net/kaerbuka/article/details/95180890; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1587953820; dc_sid=773349f394188ca3ecb72de63cd2297e; c-toolbar-writeguide=1; c_adb=1; SESSION=c6a20ff4-ff02-4e80-986c-d076e92aa534; UserName=qq_45473744; UserNick=%E4%B8%8D%E7%9F%A5%E4%BC%A4%E5%BF%83; AU=FD2; UN=qq_45473744; p_uid=U000000; UserInfo=78e6c493fcdd4d41a2bb717e4517535b; UserToken=78e6c493fcdd4d41a2bb717e4517535b; BT=1587957839642; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_7201804910-1587953817362-908392!5744*1*qq_45473744; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblog.csdn.net%252Fblogdevteam%252Farticle%252Fdetails%252F105203745%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; c_ref=https%3A//blog.csdn.net/qq_45473744; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1587958099; dc_tos=q9fgir',
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
