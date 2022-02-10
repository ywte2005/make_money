"""
@Author  : 亚博
@Time    : 2021/9/6 5:51 下午
@introduction ：
    1.
"""
import requests
import re
import hashlib
import execjs

key_word = "测试"
html_url = f'https://www.zhihu.com/search?type=content&q={key_word}'
html_text = requests.get(html_url, headers={
    "referer": "https://www.zhihu.com/search?type=content&q=%E6%B5%8B%E8%AF%95",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}).text
encoded_params = re.findall('"encodedParams":"(.*?)"', html_text, re.M | re.I)
if encoded_params:
    encoded_params = encoded_params[0]
    print(encoded_params)
else:
    print("没有获取到")
