"""
@Author  : 亚博
@Time    : 2021/9/26 11:12 上午
@introduction ：
    1. 解密参数
"""
import time

import ddddocr
import execjs
import requests
from lxml import html

ocr = ddddocr.DdddOcr()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}


def get_img(img_url):
    img_con = requests.get(img_url, headers).content
    return img_con


def de_lenovo():
    js_con = open("js/lenovo.js").read()
    js = execjs.compile(js_con, cwd="node_modules")
    d = js.call("get_d")
    img_con = get_img(f'https://passport.lenovo.com.cn/capt/1.2/getimage?source=uss.test&t={d}')
    img_res = ocr.classification(img_con)
    skey_response = requests.get(
        "https://passport.lenovo.com.cn/wauthen2/wauth/jsp/ilogin.jsp?lenovoid.action=uilogin&lenovoid.realm=support.lenovo.com.cn&lenovoid.iframestate=wechat&lenovoid.cb=https://support.lenovo.com.cn/lenovoid/lenovoid.aspx",
        headers=headers).text
    parse_skey = html.fromstring(skey_response)
    skey = parse_skey.xpath("//input[@class='jsSNum']/@value")[0]
    snum = js.call("get_snum", skey)
    data = {
        "type": "1",
        "snum": snum,
        "skey": skey,
        "c": img_res,
        "t": d,
        "iframe": "2"
    }
    return data


def de_baidu():
    js_con = open("js/lenovo.js").read()
    js = execjs.compile(js_con, cwd="node_modules")
    random = js.call("random", "8")
    response = requests.get(
        f"https://jiameng.baidu.com/portal/com/token?ajax=1&accessid=1312813949D0&device=pc&random={random}",
        headers=headers).json()
    token = response["data"]["token"]
    return random, token


if __name__ == '__main__':
    timestamps = time.time()
    print(timestamps)
