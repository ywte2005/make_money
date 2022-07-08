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
@Time    : 2022/2/25 11:46 上午
@introduction ：
    1. frida hook app端口的md5加密
"""

import frida, sys


def on_message(message, data):
    if message["type"] == "send":
        print("[*] {0}".format(message["payload"]))
    else:
        print(message)


js_code = """
Java.perform(function () {
    var messageDigest=Java.use('java.security.MessageDigest');
    // update
    for(var i = 0; i < messageDigest.update.overloads.length; i++){
        messageDigest.update.overloads[i].implementation = function(){
            var name=this.getAlgorithm()
            send("================="+name+"====================");
            send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
            if(arguments.length == 1){
                send(arguments[0]);
                this.update(arguments[0]);
            }else if(arguments.length == 3){
                send(arguments[0]);
                send(arguments[1]);
                send(arguments[2]);
                this.update(arguments[0],arguments[1],arguments[2]);
            }
        }
    }

});

"""

process = frida.get_usb_device().attach("自毁程序密码")
script = process.create_script(js_code)
script.on("message", on_message)
print("[*] Running")
sys.stdin.read()
