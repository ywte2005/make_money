"""
@Author  : 亚博
@Time    : 2021/9/10 3:45 下午
@introduction ：
    1. 
"""
import requests
from lxml import html
import base64
import ddddocr
import re

url = 'https://match.yuanrenxue.com/api/match/4'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0"
}
ocr = ddddocr.DdddOcr()
response = requests.get(url, headers).json()["info"]
parse_html = html.fromstring(response)
td_list = parse_html.xpath("//td")
result_list = []
for td in td_list:
    number_list = []
    img_list = []
    Offset = 0
    for img in td.xpath("./img"):
        src = img.xpath("./@src")[0]
        style = img.xpath("./@style")[0]
        xh = float(re.findall(r'left:(.*?)px', style)[0])
        if "none" in style:
            print("1111")
            continue
        xh += Offset
        Offset = xh
        img_list.append({"src": src, "xh": xh})

    new_list = sorted(img_list, key=lambda key: key["xh"])
    for img_ in new_list:
        zhi = img_["src"]
        img_url = zhi.split(",")[1]
        img_con = base64.b64decode(img_url)
        res = ocr.classification(img_con)
        number_list.append(res)
    resu = "".join([str(i[0]) for i in number_list])
    result_list.append(resu)
    #
print(result_list)
