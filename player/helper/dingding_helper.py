# -*- coding:utf-8 -*-
"""
@author: GXJ
@file: dingding_helper.py
@time: 2020/8/16 20:04
@desc: dingding to give an alarm function
"""
import requests
import json


def remind(message):
    """
       商品信息提醒
    """
    url = 'https://oapi.dingtalk.com/robot/send?access_token=0994057ce08c170c87c14abb5c9f54731d86bdf99cace4221f185e81e09109a9'
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        },
        "at": {
            "isAtAll": 'false'
        }
    }
    session = requests.session()
    session.headers['Content-Type'] = 'application/json'
    session.post(url=url, data=json.dumps(data), verify=False, timeout=60)


# remind('test')
