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
@Time    : 2022/4/24 11:47
@introduction ：
    1. 
"""
import re
import requests
import time
import random
import numpy as np
import math
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
import ddddocr

det = ddddocr.DdddOcr(det=False, ocr=False)


def requests_url():
    url = "https://captcha.fengkongcloud.cn/ca/v1/register?data=%7B%7D&sdkver=1.1.3&callback=sm_" + str(
        time.time()) + "&channel=DEFAULT&appId=default&rversion=1.0.3&lang=zh-cn&model=slide&organization=eR46sBuqF0fdw7KWFLYa"
    response_json = requests.get(url, headers=headers).text
    img_info = re.findall('"bg":"(.*?)".*?"fg":"(.*?)".*?"rid":"(.*?)"', response_json)[0]
    bg_img = "https://castatic.fengkongcloud.cn" + img_info[0]
    fg_img = "https://castatic.fengkongcloud.cn" + img_info[1]
    rid = img_info[2]
    return bg_img, fg_img, rid


def get_img_url(bg_img, fp_img):
    bg_img_byte = requests.get(bg_img, headers=headers).content
    fp_img_byte = requests.get(fp_img, headers=headers).content
    return bg_img_byte, fp_img_byte


def get_trace_and_times(distance):
    x = [0, 0]
    y = [0, 0, 0]
    z = [0]
    count = np.linspace(-math.pi / 2, math.pi / 2, random.randrange(20, 30))
    func = list(map(math.sin, count))
    nx = [i + 1 for i in func]
    add = random.randrange(10, 15)
    sadd = distance + add
    x.extend(list(map(lambda x: x * (sadd / 2), nx)))
    x.extend(np.linspace(sadd, distance, 3 if add > 12 else 2))
    x = [math.floor(i) for i in x]
    for i in range(len(x) - 2):
        if y[-1] < 30:
            y.append(y[-1] + random.choice([0, 0, 1, 1, 2, 2, 1, 2, 0, 0, 3, 3]))
        else:
            y.append(y[-1] + random.choice([0, 0, -1, -1, -2, -2, -1, -2, 0, 0, -3, -3]))
    for i in range(len(x) - 1):
        z.append((z[-1] // 100 * 100) + 100 + random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]))
    trace = list(map(list, zip(x, y, z)))
    times = trace[-1][-1] + random.randint(1, 5)
    return trace, times


def run():
    bg_img, fg_img, rid = requests_url()
    bg_img_byte, fp_img_byte = get_img_url(bg_img, fg_img)
    res = det.slide_match(fp_img_byte, bg_img_byte)
    random_num,times= get_trace_and_times(res["target_y"])
    return random_num,times,rid


if __name__ == '__main__':
    print(run())
