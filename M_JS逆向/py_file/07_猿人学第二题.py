"""
@Author  : 亚博
@Time    : 2021/9/10 10:33 上午
@introduction ：
    1. 
"""
import requests
import execjs

js_con = open("../js/07.js").read()
node_js = execjs.compile(js_con, cwd="node_modules")
result = node_js.call("result")
print(result)
#
res = requests.get('https://match.yuanrenxue.com/api/match/2',headers={"cookie":"m="+result})
print(res.text)
