"""
@Author  : 亚博
@Time    : 2021/9/1 4:17 下午
@introduction ：
    1. js练习题调用js包
"""
import execjs


key='service_methodGetUserCartservice_namedemander.AdStarDemanderServicesign_strict1system_type1e39539b8836fb99e1538974d3ac1fe98'
Passwd = execjs.compile(open(r"../js/01.js").read())
print(Passwd.call('get_data')[:16])
