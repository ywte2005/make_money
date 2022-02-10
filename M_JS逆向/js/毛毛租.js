var CryptoJS = require("./2.5.3-crypto-min")

function mydecrypt(e, a) {
    e = CryptoJS.enc.Utf8.parse(e);
    var l = CryptoJS.AES.decrypt(a, e, {
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7,
        iv: e
    });
    return CryptoJS.enc.Utf8.stringify(l).toString()
}

function myencrypt(e, a) {
    return e = CryptoJS.enc.Utf8.parse(e),
        a = CryptoJS.enc.Utf8.parse(a),
        CryptoJS.AES.encrypt(a, e, {
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
            iv: e
        }).toString()
}


console.log(myencrypt("55b3b62613aef1a0", '{"Type":"0","page":1,"expire":1634196589730}'))