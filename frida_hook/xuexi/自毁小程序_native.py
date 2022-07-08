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
@Time    : 2022/2/24 3:51 下午
@introduction ：
    1. 
"""
import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


js_code = """
function main2(){
    var android_dlopen_ext =Module.findExportByName(null,"android_dlopen_ext");
    console.log(android_dlopen_ext);
    if(android_dlopen_ext!=null){
        Interceptor.attach(android_dlopen_ext,{
            onEnter:function (args){
                var soName = args[0].readCString();
                if(soName.indexOf("libsscronet.so")!=-1){

                    this.hook = true
                    console.log("this.hook = true")
                }

            },
            onLeave:function (retvel){
                if(this.hook){
                    dlopentodo();
                }
            }

        });

    }
}
function dlopentodo(){
        var ver = Module.findExportByName('libsscronet.so',"SSL_CTX_set_custom_verify");
        console.log(ver)
        var custom_verify = new NativeFunction(ver,"pointer",["pointer","int","pointer"]);
        var self = new NativeCallback(function (arg1,arg2,arg3){
            hookCallBack(arg3);
            console.log("custom_verify call:",arg2,arg3);
            return custom_verify(arg1,0,arg3);
        },'pointer',["pointer","int","pointer"]);
        Interceptor.replace(ver,self);

}


function hookCallBack(p){
    var fun =new NativeFunction(p,"int",["pointer","pointer"]);
    var self = new NativeCallback(function (arg1,arg2){
        console.log("cononono",fun(arg1,arg2));
        return 0;
    },"int",["pointer","pointer"]);
    Interceptor.replace(fun,self);
}
setImmediate(main2);
"""
process = frida.get_usb_device().attach("抖音")

script = process.create_script(js_code)
script.on("message", on_message)
print("[*] Running")
script.load()
sys.stdin.read()
