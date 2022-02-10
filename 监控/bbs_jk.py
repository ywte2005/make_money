"""
@Author  : 亚博
@Time    : 2021/10/11 5:04 下午
@introduction ：
    1. 
"""
import time

import requests
from lxml import html

from toemail import WBYiSmtp

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}
url = 'https://bbs.nightteam.cn/index-{}.htm'
while 1:
    for i in range(1, 3):
        html_str = requests.get(url.format(i), headers=headers).text
        parse_html = html.fromstring(html_str)
        li_list = parse_html.xpath("//div[@class='media-body']")
        ret = WBYiSmtp()
        for li in li_list:
            status = li.xpath(".//div//span[1]//text()")
            if status:
                status = "".join(status)
                if "小时前" in status.strip():
                    href = "https://bbs.nightteam.cn/" + li.xpath(".//div[@class='subject break-all']/a/@href")[0]
                    title = li.xpath(".//div[@class='subject break-all']/a//text()")[0]
                    ret.send_email("有最新发表文章：\n 文章标题：" + title + "\n 链接：" + href)

    time.sleep(3600)
