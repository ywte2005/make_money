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
import time

import requests
from lxml import html

from helper.proxies_helper import get_proxies, change_ip


class FeiGuaKey():
    def __init__(self):
        self.url = "https://dy.feigua.cn/PromotionSearch/Search"
        self.data_info = {
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
            "page": 2
        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "Referer": "https://dy.feigua.cn/Member",
            "Cookie": "_uab_collina=162804914323587615500207; Hm_lvt_b9de64757508c82eff06065c30f71250=1634805763,1635757158; Hm_lpvt_b9de64757508c82eff06065c30f71250=1635757158; chl=key=feigua2; Hm_lvt_876e559e9b273a58993289470c10403b=1634805766,1635757207; ASP.NET_SessionId=llhkajw1sugqmx0ern04wiru; FEIGUA=UserId=66fd8774a8383acb&NickName=59f9f1499a33117c23e3245ec207c423&checksum=e48c0d3d563a&FEIGUALIMITID=96ffbf0bfc9b4afda90f3c59cf76f783; a97ac1384004b39dfb75b7b8d065e5ce=11c014ebad67002f7ad1f454a99db94f1035e547c46a7dd58ff94709b7e00ba23c566e31b3529eca7ba8db3a558533d07c04e6f381e7b74182df7fa8f878f8a43968d8c99a10963c8e02f26027d2576d0c4c4e0d1125fd0111b9d7e5b2c23513f4cbad7d7115a3f295e8bed753af7c44; SaveUserName=; Hm_lpvt_876e559e9b273a58993289470c10403b=1635757269",
            "Host": "dy.feigua.cn",
            "Origin": "https://dy.feigua.cn"
        }
        self.keywords = ["薇诺娜"]
        self.sleep_date = 20
        self.an_url = "https://dy.feigua.cn/GoodsNew/LoadBloggerAnalysis?Gid={}&promotionId={}&startTime=&endTime=&_={}"

    def request_html(self, page):
        self.headers["page"] = page
        count = 0
        while True:
            if count > 5:
                return None
            else:
                try:
                    html_response = requests.post(self.url, headers=self.headers, timeout=3, proxies=get_proxies())
                    time.sleep(self.sleep_date)
                    if html_response.status_code == 200:
                        parse_html = html.fromstring(html_response)
                        id_list = parse_html.xpath("//div[@id='ps_result_content2']/a/@data-promotionid")
                        item_list = [i.strip() for i in parse_html.xpath("//div[@class='item-title']/text()[2]")]
                        if id_list and item_list:
                            return dict(zip(id_list, item_list))
                        else:
                            return None
                    else:
                        count += 1
                        print(html_response.status_code)
                        continue
                except Exception as e:
                    print(e)
                    count += 1

    def requests_anchor(self, goods_id):
        count = 0
        while True:
            if count > 5:
                return None
            else:
                try:
                    html_response = requests.get(self.an_url.format(goods_id, goods_id, int(time.time())),
                                                 headers=self.headers, timeout=3, proxies=get_proxies())
                    time.sleep(self.sleep_date)
                    if html_response.status_code == 200:
                        parse_html = html.fromstring(html_response)
                        anchor_info = parse_html.xpath("//table[@class='table']//tr/td")
                        if anchor_info:
                            return anchor_info
                        else:
                            return None
                    else:
                        count += 1
                        print(html_response.status_code)
                        continue
                except Exception as e:
                    print(e)
                    count += 1

    def feigua_spider(self):
        for key in self.keywords:
            for page in range(1, 100):
                id_item = self.request_html(page)
                if id_item:
                    break
                else:
                    for goods_id, item_title in id_item.items():
                        anchor_info = self.requests_anchor(goods_id)


a = {"a": 1, "b": 2}

for x, z in a.items():
    print(x, z)
