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
@Time    : 2022/2/10 10:26 上午
@introduction ：
    1. 阿里自毁小程序hook学习
"""
import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jsCode_onCreate = """
Java.perform(function () {
    var OkHttpClient = Java.use("okhttp3.OkHttpClient");
    OkHttpClient.newCall.implementation = function (request) {
        var result = this.newCall(request);
        console.log(request.toString());
        return result;
    };
})
"""

# 定位jar包
process = frida.get_usb_device().attach("约苗")
# 传入上面的js代码创造脚本
script = process.create_script(jsCode_onCreate)
# 接受信息打印信息模块
script.on('message', on_message)
print('[*] Running')
script.load()
sys.stdin.read()
