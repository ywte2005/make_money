# -*- coding: utf-8 -*-
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
@Time    : 2021/11/1 17:16 下午
@introduction ：
    1. 临时任务
    2. 商品搜索关键字
    3. 以直播带货为主
    4. 30天直播销量
"""

import feapder
from feapder.utils import tools


class FirstSpider(feapder.AirSpider):
    urls = "https://dy.feigua.cn/PromotionSearch/Search"
    data_info = {
        "keyword": "薇诺娜",
        "yjbl": "",
        "hpl": "",
        "ShopScore": "",
        "SendFrom": "",
        "hasCoupon": "-1",
        "recommendTag": "0",
        "MainSalesModel": "2",
        "MainSalesRatio": "0.5",
        "viewPattern": "2",
        "sort": "4",
        "goodsprop": "[]",
        "page": "2"
    }

    def start_requests(self):
        keywords = ["薇诺娜"]
        for key in keywords:
            while 1:
                yield feapder.Request()

    def download_midware(self, request):
        pass

    def parse(self, request, response):
        title_list = response.xpath("//div[@class='postTitle']/a/span/text()").getall()
        for title in title_list:
            print(title.strip())


if __name__ == "__main__":
    FirstSpider().start()
    print(tools.get_md5(122))
