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
@Time    : 2021/12/9 10:59 上午
@introduction ：
    1. 获取京东9.9秒杀
"""
import json
import time

from fake_useragent import UserAgent
import requests

from player.helper.dingding_helper import remind

headers = {
    "User-Agent": UserAgent().chrome
}


def get_jd_ms_html():
    """
    获取9.9元秒杀
    :return:
    """
    url = "https://api.m.jd.com/api?appid=o2_channels&client=pc&functionId=pcParitySeckillGoods&body=%7B%22categoryId%22%3A3%2C%22tabId%22%3A0%7D&callback=jsonp&_=" + str(
        int(time.time() * 1000))
    headers["referer"] = "https://miaosha.jd.com/"
    s = requests.session()
    for i in range(6):
        try:
            html_text = s.get(url, headers=headers, timeout=10).text
            json_data = json.loads(html_text[6:-1])
            return json_data
        except:
            time.sleep(10)
            return None


def parse_jd_ms_json(json_data, need_list):
    email_content = "京东9.9秒杀信息\n 当前获取：{}\n****************************************\n".format("、".join(need_list))
    for data in json_data["floorList"]:
        goods_info = data["goodsInfo"]
        # 商品链接
        goods_url = "https://item.m.jd.com/product/{}.html".format(goods_info['wareId'])

        # 商品名称
        goods_name = str(goods_info["wname"])
        # 秒杀价格
        miaosha_price = str(goods_info["miaoShaPrice"])
        # 激动价格
        try:
            jd_price = str(goods_info["jdPrice"])
        except:
            jd_price = ""
        # 价格日信息
        try:
            lowest_price_days_info = goods_info['lowestPriceDaysInfo']
        except:
            lowest_price_days_info = ""
        # 简单描述
        try:
            operate_term = goods_info["operateTerm"]
        except:
            operate_term = ""
        if need_list:
            for i in need_list:
                if i in goods_name:
                    # 发送消息
                    email_content += "商品名称： " + goods_name + "\n" + "商品秒杀价:" + miaosha_price + "\n" + "商品京东价：" + jd_price + "\n" + "历史最低天数:" + lowest_price_days_info + "\n" + "简单描述：" + operate_term + "\n" + "商品链接：" + goods_url + "\n****************************************\n"
        else:
            return "没有添加您想要的商品"

    return email_content


def jd_run():
    need_list = ["肉"]
    # 京东
    jd_json = get_jd_ms_html()
    if jd_json:
        email_content = parse_jd_ms_json(jd_json, need_list)
        remind(email_content)
    else:
        remind("没有抓取到京东信息")


if __name__ == '__main__':
    jd_run()
