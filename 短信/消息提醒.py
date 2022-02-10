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
@Time    : 2021/12/13 4:34 下午
@introduction ：
    1. 
"""
# -*- coding: utf-8 -*-
from time import sleep
from datetime import datetime
import requests
from lxml import etree




def get_page(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.text if r.status_code == 200 else None


def parse_page(html):
    html = etree.HTML(html)
    forecasts = html.xpath('/html/body/div[8]/div[1]/div[1]/div[2]/ul/li/a[1]/@title')
    forecasts = '\n'.join(forecasts)
    keys = html.xpath('/html/body/div[8]/div[2]/div[6]/ul/li/b/text()')
    values = html.xpath('/html/body/div[8]/div[2]/div[6]/ul/li/a/p/text()')
    day_info = {i: values[keys.index(i)] for i in keys}
    message = '青哥哥今日提醒:\n\n' + '南京今日生活指数:\n' + '\n'.join(
        ['{}: {}'.format(i, day_info[i]) for i in day_info]) + '\n' * 3 + '南京主要地区天气预报:\n' + forecasts
    return message


def get_time():
    time = datetime.now().strftime('%H:%M:%S')
    return time


clock = '06:00:0{}'  # 设置启动时间
interval = 3  # 设置时间间隔
time_zone = [clock.format(i) for i in range(interval)]


def main():
    url = 'http://www.tianqi.com/nanjing/'
    html = get_page(url)
    message = parse_page(html)



if __name__ == '__main__':
    main()
