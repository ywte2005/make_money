var fs = require("fs")
// 框架工具模块
var vmtools = require("./tool/tools.node.js")

function GetCode() {
    var code = "";
    // 引入框架工具代码
    code += vmtools.GetCode() + '\r\n';
    // 引入浏览器相关
    code += fs.readFileSync(`${__dirname}/browser/EventTarget.js`) + "\r\n";
    code += fs.readFileSync(`${__dirname}/browser/WindowProperties.js`) + "\r\n";
    code += fs.readFileSync(`${__dirname}/browser/Window.js`) + "\r\n";
    code += fs.readFileSync(`${__dirname}/browser/Location.js`) + "\r\n";
    code += fs.readFileSync(`${__dirname}/browser/Navigator.js`) + "\r\n";
    code += fs.readFileSync(`${__dirname}/browser/Document.js`) + "\r\n";
    code += fs.readFileSync(`${__dirname}/browser/Screen.js`) + "\r\n";
    //引入用户自定义环境

    code += 'debugger' + "\r\n "
    return code
}

module.exports = {
    GetCode
}