"""
@Author  : 亚博
@Time    : 2021/9/7 11:31 上午
@introduction ：
    1. 
"""

import execjs
from feapder.utils import tools

key = 'text=周生如故&page=1&type=migu'
# # 'data=7aa2Ght1dCVHgyG7CeWCOIOnwkPPk73LGN2MAil8AFPWeFpu3QM0s6qULr8jtyBtMBNEn3FGLbmEQZPJk5fy&v=2'
js_con = open("../js/04_音乐.js").read()
js = execjs.compile(js_con)
print(js.call("encode", key))

# print(tools.get_md5(key))