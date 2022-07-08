import requests
import time

cookies = {
    'imed_session': '4PrHfyEJeOyNAT5EK7liuBtS6eiuv0o1_5496003',
    'cmi-user-ticket': 'RezscKJmLMUMZPaBoELGIMvpHE6W0h_5Y56aIA..',
    'secure-key': '33dc9bbf-241a-4275-afc4-d554fce7f6e6',
    'agent_login_img_code': 'd3fd943c77b549ad9d52f0b0c331aa50',
    'imed_session_tm': str(int(time.time() * 1000)),
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '109',
    'Content-Type': 'application/json',
    'Host': 'www.114yygh.com',
    'Origin': 'https://www.114yygh.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.114yygh.com/hospital/H06151001/yygh_FZYQ_79e02b4e_vir/139/source',
    'Request-Source': 'PC',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}
params = (
    ('_time', str(int(time.time() * 1000))),
)
data = '{"firstDeptCode":"yygh_FZYQ_79e02b4e_vir","secondDeptCode":"139","hosCode":"H06151001","target":"2022-04-06"}'

yy_data = {
    "hosCode": "H06151001",
    "firstDeptCode": "yygh_FZYQ_79e02b4e_vir",
    "secondDeptCode": "139",
    "dutyTime": 0,
    "treatmentDay": "2022-04-06",
    "uniqProductKey": "94b30cf7c735e452a3c53fa8688deb53ea53ceae",
    "cardType": "SOCIAL_SECURITY",
    "cardNo": "128203368001",
    "smsCode": "",
    "hospitalCardId": "",
    "phone": "15612317021",
    "orderFrom": "OTHER"
}


def get_doctor_info():
    response = requests.post('https://www.114yygh.com/web/product/detail', headers=headers, params=params,
                             cookies=cookies,
                             data=data)
    if response.status_code == 200:
        detail_data = response.json()["data"]
        for detail_date in detail_data:
            for doctor_info in detail_date["detail"]:
                if doctor_info["doctorName"] == "刘爱珍":
                    return doctor_info["doctorName"], doctor_info[
                        "uniqProductKey"]
    print("没有获取到指定医生信息", response.text)
    return None, None


def yy_requests(keyword):
    yy_data["uniqProductKey"] = keyword
    response = requests.post('https://www.114yygh.com/web/order/save', headers=headers, params=params,
                             cookies=cookies,
                             data=yy_data)
    if response.status_code == 200:
        return response.json()["data"]["orderNo"]
    print(response.text)
    return None


def yy_status():
    params_ = (
        ('_time', '1648801451016'),
        ('idCardType', 'IDENTITY_CARD'),
        ('idCardNo', '130726199710126911'),
        ('orderStatus', 'BOOKING_SUCCESS'),
        ('pageNo', '1'),
        ('pageSize', '10'),
    )
    headers_ = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'www.114yygh.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.114yygh.com/personal/order',
        'Request-Source': 'PC',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    response = requests.post('https://www.114yygh.com/web/order/list', headers=headers_, params=params_,
                             cookies=cookies)
    if response.status_code == 200:
        json_data = response.json()["data"]
        if "预约成功" in json_data:
            return 1

        return 0
    return 0


def main():
    # 获取用户key信息条件
    # doctor_name, key = get_doctor_info()
    # print(doctor_name, key)
    # 发送预约请求，获取NO编号
    # order_no = yy_requests(key)
    # print(order_no)
    # 获取预约状态
    status = yy_status()
    print(status)


if __name__ == '__main__':
    main()
