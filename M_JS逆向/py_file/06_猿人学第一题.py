"""
@Author  : 亚博
@Time    : 2021/9/9 5:27 下午
@introduction ：
    1. 
"""
import execjs

js_con = open("../js/06_猿人学第一题.js").read()
js = execjs.compile(js_con, cwd="node_modules")
result = js.call("oo0O0", "1631279772000")
print(result)
