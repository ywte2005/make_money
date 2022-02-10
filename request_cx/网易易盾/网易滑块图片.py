"""
   ┌─┐       ┌─┐ + +
┌──┘ ┴───────┘ ┴──┐++
│                 │
│       ───       │++ + + +
███████───███████ │+
│                 │+
│       ─┴─       │
│                 │
└───┐         ┌───┘
    │         │
    │         │   + +
    │         │
    │         └──────────────┐
    │                        │
    │                        ├─┐
    │                        ┌─┘
    │                        │
    └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
      │ ─┤ ─┤       │ ─┤ ─┤
      └──┴──┘       └──┴──┘  + + + +
             神兽保佑
            代码无BUG!
            
@Author  : 亚博
@Time    : 2021/11/29 2:19 下午
@introduction ：
    1. 请求滑块图片链接
    2. 加密FP和CB
"""
import execjs
import requests

js_file_cb = open("/Users/huan/make_money  /M_JS逆向/js/网易de_cb.js").read()
js_file_fp = open("/Users/huan/make_money  /M_JS逆向/js/网易de.js").read()

js_str_cb = execjs.compile(js_file_cb)
js_str_fp = execjs.compile(js_file_fp)
cb_result = js_str_cb.call("_0x52dc7e")
fp_result = js_str_fp.call("result")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
}
data = {
    "referer": "https%3A%2F%2Fdun.163.com%2Ftrial%2Fjigsaw",
    "zoneId": "CN31",
    "id": "07e2387ab53a4d6f930b8d9a9be71bdf",
    "fp": fp_result,
    "https": "true",
    "type": "2",
    "version": "2.16.0",
    "dpr": "2",
    "dev": "1",
    "cb": cb_result,
    "ipv6": "false",
    "runEnv": "10",
    "group": "",
    "scene": "",
    "lang": "zh-CN",
    "width": "320",
    "audio": "false",
    "token": "",
    "callback": "__JSONP_cik0cd2_0"
}
url = "https://c.dun.163.com/api/v2/get"
response_json = requests.get(url, headers=headers,params = data).text
print(response_json)
