"""
@Author  : 亚博
@Time    : 2021/9/1 4:17 下午
@introduction ：
    1. js练习题调用js包
"""
import execjs
# ab4b05cf502dc2623e1d7164bf6c878e
key = 'service_methodGetUserCartservice_namedemander.AdStarDemanderServicesign_strict1system_type1e39539b8836fb99e1538974d3ac1fe98'
js_con = open(r"../js/星图sign.js").read()
Passwd = execjs.compile(js_con)
result = Passwd.call("result", key, "")
print(result)
