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
@Time    : 2022/4/6 11:27
@introduction ：
    1. 酷安app-9.2.2 请求有token
"""
import frida, sys


def on_message(message, data):
    if message["type"] == "send":
        print("[*] {0}".format(message["payload"]))
    else:
        print(message)


hook_code = """
// 获取方法的基地址
var get_as_add=Module.getExportByName("libnative-lib.so","getAuthString");
// 获取so文件的基地址
var native_lib_base_add=parseInt(get_as_add)-parseInt("0xA8320");
// prt 指针
send("native_lib_base_add"+ptr(native_lib_base_add))
"""

process = frida.get_usb_device().attach("酷安")
script = process.create_script(hook_code)
script.on("message", on_message)
print("[*] running")
sys.stdin.read()
