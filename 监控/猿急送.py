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
@Time    : 2022/2/17 5:10 下午
@introduction ：
    1. 获取猿急送信息邮件返回
"""
import requests

from to_email import WBYiSmtp
from lxml import html

url = "https://www.yuanjisong.com/job/allcity/zxfb/page1"
keyword = ["爬取", "爬虫", "抓取", "采集"]
html_text = requests.get(url).text
parse_html = html.fromstring(html_text)
div_list = parse_html.xpath("//div[@class='consultant_title margin_top_15']")
ret = WBYiSmtp()


def parse_title(div):
    for key in keyword:
        if key in title or key in des:
            task_time = div.xpath(".//p[2]/span[3]/text()")[0]
            task_price = div.xpath(".//p[3]/span/text()")[1]
            task_url = div.xpath("./a[1]/@href")[0]
            content = "标题：" + title + "\n" + \
                      "简介：" + des + "\n" + \
                      "工时：" + task_time + "\n" + \
                      "价格：" + task_price + "\n" + \
                      "链接：" + task_url + "\n"
            return content
    return None


for div in div_list:
    title = div.xpath(".//b/text()")[0]
    des = div.xpath(".//a[2]/p[@class='margin_bottom_10']/text()")[0]
    content = parse_title(div)
    if content:
        ret.send_email("猿急送：" + "\n" + content)
