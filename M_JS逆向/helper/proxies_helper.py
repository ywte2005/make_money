# -*- coding:utf-8 -*-
"""
@author: GXJ
@file: proxies_helper.py
@time: 2020/9/23 10:33
@desc: 
"""
import requests


def get_proxies():
    proxy_host = "http-proxy-t1.dobel.cn"
    proxy_port = "9180"
    proxy_user = "WEIBOYIHTT3"
    proxy_pass = "FRbg35CW1"
    proxy_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxy_host,
        "port": proxy_port,
        "user": proxy_user,
        "pass": proxy_pass,
    }
    proxies = {
        "http": proxy_meta,
        "https": proxy_meta,
    }
    return proxies


def change_ip():
    """
    切换隧道IP
    :return:
    """
    url = 'http://ip.dobel.cn/switch-ip'
    requests.get(url, proxies=get_proxies())
