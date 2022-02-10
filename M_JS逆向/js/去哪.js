const jsdom = require("jsdom");
const {JSDOM} = jsdom;
const dom = new JSDOM(` < !DOCTYPE html > <p > Hello world < /p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;

var qtTime = [83, 80, 56, 56, 58];
var cookieToken = [83, 80, 54, 58];
var tokenStr = [115, 119, 112, 99, 116, 97, 99, 114, 107, 97, 118, 113, 109, 103, 112]


var cookie="QN1=00008480306c38480ad8b9ad; QN300=s%3Dbaidu; QN99=8505; QunarGlobal=10.86.213.149_-66262970_17c2a2ea5f3_149f|1632795483952; QN601=9b127e9646e0395172e4c38dea06124b; _i=ueHd8Z6RdjYXkkhAUYq18heVCfXX; QN269=503F6C80200211EC9BE4FA163EEFDE16; QN48=00008b802f1038480ae8bed3; fid=59c04754-bf0e-4450-80be-258ea4596fae; Alina=88e502c5-b13075-4245dd11-87815e93-499561527b6c; QN170=223.72.60.56_738278_0_VMYD%2B8sOis1iPy919%2F09bhhiqsNa4GVHed%2Bpj4CZ2iQ%3D; quinn=43ba217664638c9c523e4abbd5297abd0097ca0a787141751b9b8b941d301a7699db02c0c5d5df4bdcc94a29b2ed00ff; SC1=9483ef1e5a3d114bf651b1cd05754b16; SC18=; QN205=organic; QN277=organic; QN66=qunar; csrfToken=9Ep5JFQ9qUps9TRMgr5gnkLk7EF2FBRP; qunar-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; QN621=1490067914133%3DDEFAULT%26fr%3Dqunarindex; QN667=A; _vi=j4yisTEP3PRCw4PzjTDPWOQexclRbkMdz27Akz9ld4I3L9yvNMzt_fMzO1NXAYOAjxNTmtqvWvOo_kZ9OgZEcPH1MdYligQAVjVg5fvCFTyC2dKf2d44fpGzjv3Vr2BSL9Pe1N0CEAg5w6PvUUvB73v2eBuw450tfz-9HuQMFz1A; QN271=280da21f-b89e-47d6-bc64-ab78028f9c6d; F235=1634867382941; QN668=51%2C56%2C53%2C54%2C58%2C56%2C57%2C53%2C58%2C52%2C59%2C56%2C51; QN267=1466952422607ff79f"

function dencryptCode(t) {
    return t.map(function (e) {
        return String.fromCharCode(e - 2)
    }).join("")
}

function getQtTime(t) {
    return t ? Number(t.split(",").map(function (e) {
        return String.fromCharCode(e - 2)
    }).join("")) : 0
}

function getCookie(t) {
    var n =cookie.split("; ");
    for (var r = 0; r < n.length; r++) {
        var i = n[r].split("=");
        if (i[0] === t) {
            return decodeURIComponent(i[1])
        }
    }
    return null
}

function getTokenStr() {
    var t = dencryptCode(tokenStr);
    var n = document.getElementById(t);
    var r = n && n.innerHTML;
    return r ? r : getCookie(dencryptCode(cookieToken))
}

function encrypt() {
    var t = getTokenStr()
        , n = getQtTime(getCookie(dencryptCode(qtTime)))
        , r = n % 2;
    return t + n
}

console.log(encrypt())