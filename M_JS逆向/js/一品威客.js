var CryptoJS = require('./2.5.3-crypto-min.js');
l = {
    key: CryptoJS.enc.Utf8.parse("fX@VyCQVvpdj8RCa"),
    iv: CryptoJS.enc.Utf8.parse(function (t) {
        for (var e = "", i = 0; i < t.length - 1; i += 2) {
            var r = parseInt(t[i] + "" + t[i + 1], 16);
            e += String.fromCharCode(r)
        }
        return e
    }("00000000000000000000000000000000"))
}
    , h = function (data) {
    return function (data) {
        return CryptoJS.AES.encrypt(data, l.key, {
            iv:l.iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    }(data)
}
console.log(h("83fcb26aa3114f8ea29f7d66ce747955"))
