var CryptoJS = require("./2.5.3-crypto-min")


function result(t, e) {
    var a = CryptoJS.enc.Utf8.parse(e);
    try {
        var s = CryptoJS.DES.encrypt(String(t), a, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        })
    } catch (t) {
        console.log(t)
    }
    return s.toString()
}


console.log(result("123456", "e9284d45-cf2a-4e46-9367-f122413ca6b0"))