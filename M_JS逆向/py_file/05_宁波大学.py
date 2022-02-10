"""
@Author  : 亚博
@Time    : 2021/9/8 3:00 下午
@introduction ：
    1. 
"""
import execjs

js_con = open(r"../js/05_宁波大学.js").read()
js = execjs.compile(js_con, cwd="node_modules")
result = js.call("encryptAES", "234", "27Z551GW3kvCUv6k")
print(result)
