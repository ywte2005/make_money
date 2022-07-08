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
@Time    : 2022/2/16 11:41 上午
@introduction ：
    1. 
"""
import requests

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
    'x-sgext': 'JAP2Ga4J0U5VrwgDyM2%2BNhnHKcQtxzrPIcAr1SHCOsQ1xjXGNcY1xjXGNcY1xjXGNcY1xjXGNcY1xjXGNcY6xy%2FCLc8hxy7DLNUpxHqUKcYpxy3DesYqwn2UOsY6zjqULdUpxinBOsM6xzrHOsc6xzrEOsc6xzrPOsQ6xDrHOsY6xjrGOsY6xjrVfA%3D%3D',
    'umid': 'Ygt1BKDIrBMDAFP3hdSvjB6N',
    'x-sign': 'azU7Bc002xAAJKcDd7SZt6NBfuYCRKcEqLJ3woCmXMywuWcPlQAUwWCExyNIwNanHAi7FTBdGcFUTmN49z3jAAZABpSnJKcEpySnBK',
    'x-sid': '15f2b0eb062b82931d8bbf911aa90610',
    'x-uid': '3295445505',
    'x-nettype': 'WIFI',
    'x-pv': '6.3',
    'x-nq': 'WIFI',
    'EagleEye-UserData': 'spm-cnt=a2170.13730683.0.0&spm-url=a2170.7905589.rights.1',
    'first_open': '1',
    'x-features': '27',
    'x-app-conf-v': '0',
    'x-mini-wua': 'HHnB_6rb%2FxTeyXxwznBZ18%2BJYpk%2F5qG2C6f3VAY6fSk9o3vyIR2Jfzq5o1N1k8jqsqVaVOQM2RSc3uJnfIqke3q6c7Sh1JE4T0POVk0MPWWwyHab2z4rO7pB0he5JteF9sO2v5CHRSH9u60Q3U6%2BTW5JcszHEwUVY%2BOm5T2cqJU154Q0%3D',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Content-Length': '171',
    'oaid': 'b91da0d80700a696',
    'x-t': '1644982426',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'x-bx-version': '6.5.40',
    'f-refer': 'mtop',
    'x-extdata': 'openappkey%3DDEFAULT_AUTH',
    'x-ttid': '10002089%40fleamarket_android_7.1.90',
    'x-app-ver': '7.1.90',
    'x-c-traceid': 'Ygt1BKDIrBMDAFP3hdSvjB6N1644982426750008419862',
    'x-location': '116.424083%2C39.999422',
    'x-umt': 'CKsA13pLPDJpnQJ%2FAD1fFKoojcS%2Br5Iy',
    'a-orange-q': 'appKey=21407387&appVersion=7.1.90&clientAppIndexVersion=1120220215114806538&clientVersionIndexVersion=0',
    'x-utdid': 'Ygt1BKDIrBMDAFP3hdSvjB6N',
    'x-appkey': '21407387',
    'x-devid': 'AsdvCFHtUrH36Yq3ACui8mpA3m19EEmGCkgvIC-ZsWo2',
    'user-agent': 'MTOPSDK%2F3.1.1.7+%28Android%3B10%3BXiaomi%3BMI+8+SE%29',
    'Host': 'acs.m.taobao.com',
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
}

params = (
    ('data', '{"bucketWeight":60,"gps":"39.999422,116.424083","latitude":"39.999422","longitude":"116.424083","userLevel":1}'),
)

response = requests.post('https://acs.m.taobao.com/gw/mtop.taobao.idle.coin.fishing.harvest/1.0/', headers=headers, params=params)
print(response.text)

