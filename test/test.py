import execjs
import hashlib
import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'cookie': '_zap=e2037bb2-72f1-4c22-bef5-28fa54ba5518; d_c0="AsBc5n5BmhSPTr3B4rHxAlgB1PgXeNxf4Cw=|1646729318"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1659690149; _xsrf=fc64a6a9-c6b6-47fd-9e4f-1c05e705fab0; KLBRSID=b4f9781e1155b8a1bc876ec55da1029a|1659690237|1659690148; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1659690237; SESSIONID=Q7glVdIIQjSoGFQQ4F354A9XyKizgTt8T2gW6KPyQu7; JOID=U1kQB04Fn58ZW9F-SQCLS58f9bleVKz5dAm1MwFQ9ch3HZMvHKRGc35f1XtJcusz3l_dQ3HQ0nqmgKiy4lkFU1Q=; osd=Ul8XB00EmZgZWNB4TgCISpkY9bpfUqv5dwizNAFT9M5wHZAuGqNGcH9Z0ntKc-003lzcRXbQ0Xugh6ix418CU1c=',
    'referer': 'https://www.zhihu.com/search?type=content&q=Axure',
    "x-ab-param":"",
    'x-ab-pb': 'CuYBGwA/AEMARwC0AEABaQFqAXQBOwK5AswC1wLYAjIDTwNQA6ADoQOiA7cD8wP0AzMEjASNBKYE1gQRBSkFMgVRBYsFjAWeBRYGMAYxBn4GogbrBicHVwd3B3gHmwfYB9wH3QcnCGcIdAh2CHkIxQjaCOUIPwlCCVQJVQlgCY0JqwnDCcQJxQnGCccJyAnJCcoJywnMCdEJ5QnxCfQJBApJCmUKawqYCqUKqQq+CsQK1ArdCu0K/Qr+CikLOws8C0MLRgtxC3YLhQuHC40LuQvAC9cL4AvlC+YLLAw4DHEMjwysDLUL5AoScwAAFQAAAQEAAAAVAAAAAAAAAAAAAAAAAAQEAAQAAAEBAAABAAABAAIAAAEAAAAAAgIABAAABgcAAQABAAAAAAEAAAAAAAAAAAAAAAAEAwAAAAABAAAAAAEAAAQAAAEAAQAAAAAAAQAAAAAAAAACAwIAAwA=',
    'x-api-version': '3.0.91',
    'x-app-za': 'OS=Web',
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': "2.0_tUtkz9wbDdFxuQbifGjLnTXBeVCP2oQzNNDs0FvGAheJH4Wt0HdVB7WuhXhU7wf",
    'x-zst-81': "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZKRY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIoLVqr4gxrRPOI0cY7HL8qun9g93mFukyigcmebS_FwOYPRP0E4rZUrN9DDom3hnynAUMnAVPF_PhaueTFLNGu9VYArNmju39iheqxgLKXhw9Y7eG2AXC6BNMrRVyPgCmchr9xCFKebSTVMoYICSGH9wLUgXM8utmbQ3BrRp8xDNqX9HKeQ39JHcB6BL1KRgK_hUqr4XmoUp9tBV12XeB9hX_uqcqjhXOIucmfB28fgcCpUe99c9LTBw1ZCC_duFCOg_z9cP8yUYydG2CeicmqrOGV9g91UXmLrr1_9CpHDeY2ugfxceqX9HKbwN9gGXyfJOMaqCxEgCLEGOYDcU_ibx8oJxKsXXB-cpmsGLKe0S04uCMWJxCeXYs"
}

url = '101_3_3.0+/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=Axure&correction=1&offset=20&limit=20&filter_fields=&lc_idx=20&show_all_topics=0&search_hash_id=5d10e1d21b32eebfc1e97842dd1758a6&search_source=Normal&vertical_info=0%2C1%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C1+"AsBc5n5BmhSPTr3B4rHxAlgB1PgXeNxf4Cw=|1646729318"+3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZKRY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIoLVqr4gxrRPOI0cY7HL8qun9g93mFukyigcmebS_FwOYPRP0E4rZUrN9DDom3hnynAUMnAVPF_PhaueTFLNGu9VYArNmju39iheqxgLKXhw9Y7eG2AXC6BNMrRVyPgCmchr9xCFKebSTVMoYICSGH9wLUgXM8utmbQ3BrRp8xDNqX9HKeQ39JHcB6BL1KRgK_hUqr4XmoUp9tBV12XeB9hX_uqcqjhXOIucmfB28fgcCpUe99c9LTBw1ZCC_duFCOg_z9cP8yUYydG2CeicmqrOGV9g91UXmLrr1_9CpHDeY2ugfxceqX9HKbwN9gGXyfJOMaqCxEgCLEGOYDcU_ibx8oJxKsXXB-cpmsGLKe0S04uCMWJxCeXYs'
# md5_url = hashlib.md5(url.encode()).hexdigest()
# ctx = execjs.compile(open('./test.js', 'r', encoding='utf-8').read())
# x_96 = ctx.call("(0, D)", md5_url)
# headers["x-zse-96"] = "2.0_"+x_96
# print(md5_url)
# print(headers["x-zse-96"])
response = requests.get(
    'https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=Axure&correction=1&offset=20&limit=20&filter_fields=&lc_idx=20&show_all_topics=0&search_hash_id=5d10e1d21b32eebfc1e97842dd1758a6&search_source=Normal&vertical_info=0%2C1%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C1',headers=headers)

print(response.text)

# 29526c60d99deb595087ba08e572782b