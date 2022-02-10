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


jscode = """
Java.perform(function(){
    // 给类一个新的对象
    var Testsig = Java.use('com.yaotong.crackme.MainActivity');
    // 定位函数，改写类里的函数，implementation是执行的意思，是固定写法
    Testsig.securityCheck.implementation = function(str){
        send('I am here');
        return true; 
        };
    });
"""

# 定位jar包
process = frida.get_usb_device().attach("自毁程序密码")
# 传入上面的js代码创造脚本
script = process.create_script(jscode)
# 接受信息打印信息模块
script.on('message', on_message)
print('[*] Running')
script.load()
sys.stdin.read()
