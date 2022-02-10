"""
@Author  : 亚博
@Time    : 2021/10/11 11:10 上午
@introduction ：瓜子车二手网
    1. https://www.guazi.com/buy?search=%7B%22key_word%22%3A%22%E5%A4%A7%E4%BC%97POLO%22%7D
    抓取汽车列表，主要两个加密
        1.qpres 参数
        2.verify-token 请求头
"""
import time
import hashlib
import requests

urls = [
    f"https://mapi.guazi.com/car-source/carList/pcList?minor=&sourceType=&ec_buy_car_list_ab=&location_city=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&key_word=%E5%A4%A7%E4%BC%97POLO&page={page}&pageSize=20&city_filter=12&city=12&guazi_city=12&qpres=&versionId=0.0.0.0&osv=IOS&platfromSource=wa"
    for page in range(1, 3)
]
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}
stringify_params = 'adKey=pc_index_finance_pop&cityId=12&clueId=&osv=IOS&platfromSource=wap&versionId=0.0.0.0'
m = hashlib.md5()


def get_token():
    ttt = int(time.time())
    data = str(ttt) + stringify_params
    m.update(data.encode("utf-8"))
    params_md5 = m.hexdigest()
    add_par = "guaziclientuc" + params_md5
    m.update(add_par.encode("utf-8"))
    token = m.hexdigest()
    return token


def get_request(url):
    headers["verify-token"] = get_token()
    json_data = requests.get(url, headers=headers).json()
    print(json_data["data"])
    print(json_data["msg"])


def run():
    for url in urls:
        time.sleep(4)
        get_request(url)


run()