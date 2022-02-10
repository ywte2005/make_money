const jsdom = require("jsdom");
const {
    JSDOM
} = jsdom;
const dom = new JSDOM(` < !DOCTYPE html > <p > Hello world < /p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;

function shuffleArray(a) {
    for (var b, c, d = a.length; d; b = parseInt(Math.random() * d),
        c = a[--d],
        a[d] = a[b],
        a[b] = c)
        ;
    return a
}

// 联想用到的解密
function get_d() {
    for (var a = "", b = new Date, c = b.getDate(), d = b.getHours(), e = b.getMinutes(), f = b.getSeconds(), g = b.getMilliseconds(), h = c + "" + d + e + f + g, i = 0; 8 > i; i++)
        a += Math.floor(10 * Math.random() + 1);
    var j = h + "" + a;
    return j.length > 20 && (j = j.substring(0, 20)),
        j
}

function get_snum(jsSNum) {
    for (var a = jsSNum.split(""), b = jsSNum.split(""), c = shuffleArray(a), d = shuffleArray(b), e = [], f = 0; 10 > f; f++) {
        e.push(c.pop());
        e.push(d.pop());
    }

    return e.join("")
}


// 百度用到的js
function random(t) {
    for (var e = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", n = "", i = t; i > 0; --i)
        n += e[Math.floor(Math.random() * e.length)];
    return n
}
console.log(random(8))
