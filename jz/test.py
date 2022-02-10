"""
@Author  : 亚博
@Time    : 2021/10/11 10:33 上午
@introduction ：
    1. 
"""
import time

import requests
from lxml import html

urls = [
    f'https://www.chictr.org.cn/searchprojen.aspx?title=&officialname=&subjectid=&secondaryid=&applier=&studyleader=&ethicalcommitteesanction=&sponsor=&studyailment=&studyailmentcode=&studytype=0&studystage=0&studydesign=0&minstudyexecutetime=&maxstudyexecutetime=&recruitmentstatus=0&gender=0&agreetosign=&secsponsor=&regno=&regstatus=0&country=&province=&city=&institution=&institutionlevel=&measure=&intercode=&sourceofspends=&createyear=0&isuploadrf=&whetherpublic=&btngo=btn&verifycode=SGX9s&page={page}'
    for page in range(1, 10)

]
for url in urls:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }
    html_str = requests.get(url, headers=headers).text
    parse_html = html.fromstring(html_str)
    numbers = parse_html.xpath("//table[@class='table_list']//tr/td[2]//text()")
    date_str = parse_html.xpath("//table[@class='table_list']//tr/td[5]//text()")
    for n, d in zip(numbers, date_str):
        print(n.strip(), "   ", d.strip())
    time.sleep(3)
