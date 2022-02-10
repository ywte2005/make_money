"""
@Author  : 亚博
@Time    : 2021/9/26 6:39 下午
@introduction ：
    1. 
"""
import requests

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
url = 'https://www.xiaohongshu.com/discovery/item/60d80470000000002103a230?source=question'
response = requests.get(url, headers=headers).text
print(response)
