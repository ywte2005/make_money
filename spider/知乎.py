"""
@Author  : 亚博
@Time    : 2021/9/6 5:00 下午
@introduction ：
    1. 
"""
import re

import requests

keyword = "Python"
url = "https://www.zhihu.com/search?type=content&q={}".format(keyword)
headers = {
    # "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "cookie": "_zap=cbf1b562-3200-47e1-96d0-2e4b16582e2f; d_c0=\"AHDekxbSghOPTgNh5nJA5QDwTzAAFnwDFcY=|1627976740\"; __snaker__id=viRh1iIQs3lgSl8b; gdxidpyhxdE=imuBVLlSW%2FPnrkbMkm9CzSTmxEd0jfg%2BRbtLEhPJcMmHNAMvB5tThad96kxyb8Y%2ByUrMK%2FT%2FBzcBKyYx%2FmMBf9vRr1hxLPnSTJqXKAZCamAVlrpHVR%2BYImb6mR7tCjSr7R90j9l559t%2FfefLwt85nz8hffv38ULJzTIQMRgJ42gT5Xxn%3A1628238702336; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=l9tzXGwzwF2TkLxVqvnJikWhGDtIJv%2Fp6hVxCuDyE4tcx6AzzHJLLMzBVeaSt95J7P4PGUoozSC1XNWYTk98unRCdGPXdHcW%2FwKXCpecmftStfWUzSaCmUfcORTQhUx2UUM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee86e85aaa8af7b1c83efb9e8eb3c84f838f8fafb663f4baad98cd52a1ea00a8e52af0fea7c3b92ab0e7bc9bdb4db5a6b9a7b160a994b8b7f47eae96a78cd664859cbcaac97eedb0fa89d57481ab8c9ac840b8bdb8d7c472ba9886adcf47ba9e9a86e459b8e7fbabb65cf89089b6ee65ba8d8dd2db4695879c8cbc34b7b29ea4e74d9488aca9e25deda985b9c27ca7bda387f759b8ba99b6f959a39da3b6e5698d8e9cb2eb5fbcee9bb6d037e2a3; YD00517437729195%3AWM_TID=e1gQdaNIUUxBFUAFEAJqzhaJ0NNY7xXL; z_c0=\"2|1:0|10:1628237822|4:z_c0|92:Mi4xS0ZYY0V3QUFBQUFBY042VEZ0S0NFeVlBQUFCZ0FsVk5fajM2WVFCSlVkczh4NzhJRUd0OFE0U3FybHRTNHpyZVJ3|7eddd3b2cc3e81e03a833b17425921f08f60bb8b902bfd4802e6b6bfb6a320fe\"; _xsrf=246aef50-182c-4b37-b50f-d6bf78103aff; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1630898395,1630914464,1630915039,1630917728; SESSIONID=OinHUPHhpno73lARHwdjjtg1UBfgT0RALXBI9LUsDSK; JOID=UFkVCkhiag_eghGiK2m4Ub-lyCI6LgJonNZC60oTB2Hgu3zgeAC2ObSAE6ooQH6pI72sTc4nJw3ASuzeb_4qcOM=; osd=V14cBUxlbQbRhhalIma8VrisxyY9KQtnmNFF4kUXAGbptHjnfwm5PbOHGqUsR3mgLLmrSscoIwrHQ-PaaPkjf-c=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1630918421; KLBRSID=fe78dd346df712f9c4f126150949b853|1630918500|1630914462",
    "referer": "https://www.zhihu.com/search?type=content&q=%E5%93%94%E5%93%A9",
    "sec-ch-ua": "\"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "x-ab-param": "zr_slotpaidexp=1;tp_dingyue_video=0;qap_question_author=0;se_ffzx_jushen1=0;tp_topic_style=0;tp_zrec=1;tp_contents=1;qap_question_visitor= 0;zr_expslotpaid=1;pf_adjust=1;top_test_4_liguangyi=1;pf_noti_entry_num=2",
    "x-ab-pb": "CsIBUAPuBIwCmwuJDJ8CzARPAQoEdAFNBEUEnwS0CqYB9gJpAX0C4QP0A7kCogOdBOAEngSmBI4DoAPhBOkEQwBHAFcDcgN5BLcD+ANAAYkCqwP0CzQMYAs0BNEEtQt1BMwCagEyA08D8wMqBDMEhQRSC+wK3AvkCjsCxwJFA8EEAQs/AMoCVgwqAosEhAIIBEIE2gQbAAsEZATiBNgCagTPCwcM4AvXAqED4wRpBLQAbQLoA2gEbAQPC1cE1ws3DGwD9wMSYQAAAAIAAgEAAQAAAAIAAAABAQEAFQAAAAAAAAAAARUABQEAAAABBAAAAAAABAMAAAAAAAAAAAABAQAAAAABAAEAAAEAAAAAAQAAAAEyAAALAQAAAAEAAAAAAAEBAQABAAA=",
    "x-api-version": "3.0.91",
    "x-app-za": "OS=Web",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_2.0",
    "x-zse-96": "2.0_a8Oyr7r867tpcLNB1XtykTuqkXFYcM28T9YygvLqb_Yfaccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}
html_data = requests.get(url, headers=headers).content.decode("utf-8")
csib = re.findall('"encodedParams":"(.*?)"', html_data)
if csib:
    csib = csib[0]
print(csib)
