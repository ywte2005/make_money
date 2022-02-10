//雪球长文信息，js逆向

// parentId

// traceId
const jsdom = require("jsdom");
const {
    JSDOM
} = jsdom;
const dom = new JSDOM(` < !DOCTYPE html > <p > Hello world < /p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;
const getRandomValues = require('get-random-values')
var sampled = Math.random() <= 0.1


for (var u = [], d = 0; d < 256; ++d)
    u[d] = (d + 256).toString(16).substr(1);

function f(t, e) {
    var n = e || 0
        , r = u;
    return [r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]], r[t[n++]]].join("")
}

function a(t, e) {
    var r = new Uint8Array(16);
    return getRandomValues(r), r

}

function b(t, e) {
    var i = new Array(16);

    for (var t, e = 0; e < 16; e++)
        0 == (3 & e) && (t = 4294967296 * Math.random()),
            i[e] = t >>> ((3 & e) << 3) & 255;
    return i

}

function get_parentId(t) {
    return f(a()).substr(0, t)
}

function get_traceID(t) {
    return f(b()).substr(0, t)
}

function result() {
    var id = get_parentId(16)
    var parentId = get_parentId(16)
    var traceId = get_traceID()
    var e = sampled ? "01" : "00"
        , n = sampled ? id : parentId;
    return "00-" + traceId + "-" + n + "-" + e
}

console.log(result())
