h = "009c4a35d9aca4c68f1a3fa89c93684347205a4d84dc260558a049869709ac0b42"

function parseUtf8StringToHex(e) {
    for (var t = (e = unescape(encodeURIComponent(e))).length, n = [], i = 0; i < t; i++)
        n[i >>> 2] |= (255 & e.charCodeAt(i)) << 24 - i % 4 * 8;
    for (var r = [], o = 0; o < t; o++) {
        var a = n[o >>> 2] >>> 24 - o % 4 * 8 & 255;
        r.push((a >>> 4).toString(16)),
            r.push((15 & a).toString(16))
    }
    return r.join("")
}

function parseArrayBufferToHex(e) {
    return Array.prototype.map.call(new Uint8Array(e), (function (e) {
            return ("00" + e.toString(16)).slice(-2)
        }
    )).join("")
}

function multiply(e) {
    if (this.isInfinity())
        return this;
    if (!e.signum())
        return this.curve.infinity;
    for (var t = e.multiply(a), n = this.negate(), i = this, r = t.bitLength() - 2; r > 0; r--) {
        i = i.twice();
        var o = t.testBit(r);
        o !== e.testBit(r) && (i = i.add(o ? this : n))
    }
    return i
}

function multiply_n(e, t, n) {
    null != e && ("number" == typeof e ? this.fromNumber(e, t, n) : null == t && "string" != typeof e ? this.fromString(e, 256) : this.fromString(e, t))
}

function fromNumber(e, t, i) {
    if ("number" == typeof t)
        if (e < 2)
            this.fromInt(1);
        else
            for (this.fromNumber(e, i),
                 this.testBit(e - 1) || this.bitwiseTo(n.ONE.shiftLeft(e - 1), m, this),
                 this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(t);)
                this.dAddOffset(2, 0),
                this.bitLength() > e && this.subTo(n.ONE.shiftLeft(e - 1), this);
    else {
        var r = new Array
            , o = 7 & e;
        r.length = 1 + (e >> 3),
            t.nextBytes(r),
            o > 0 ? r[0] &= (1 << o) - 1 : r[0] = 0,
            this.fromString(r, 256)
    }
}

function y(e) {
    var t = multiply(new multiply_n(e, 16));
    return "04" + l.leftPad(t.getX().toBigInteger().toString(16), 64) + l.leftPad(t.getY().toBigInteger().toString(16), 64)
}

function g(e, t) {
    var n = new s
        , i = (new s).getZ(f, t.substr(2, 128))
        , r = l.hexToArray(l.arrayToHex(i).toString())
        , o = e
        , a = l.hexToArray(o)
        , c = new Array(n.getDigestSize());
    return n.blockUpdate(r, 0, r.length),
        n.blockUpdate(a, 0, a.length),
        n.doFinal(c, 0),
        l.arrayToHex(c).toString()
}

function v(e, t) {
    var n = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
        , r = n.pointPool
        , a = n.der
        , s = n.hash
        , c = n.publicKey
        , u = "string" == typeof e ? parseUtf8StringToHex(e) : parseArrayBufferToHex(e);
    s && (u = g(u, c = c || y(t)));
    var f = new i(t, 16)
        , h = new i(u, 16)
        , p = null
        , m = null
        , v = null;
    do {
        do {
            var b = void 0;
            p = (b = r && r.length ? r.pop() : A()).k,
                m = h.add(b.x1).mod(d)
        } while (m.equals(i.ZERO) || m.add(p).equals(d));
        v = f.add(i.ONE).modInverse(d).multiply(p.subtract(m.multiply(f))).mod(d)
    } while (v.equals(i.ZERO));
    return a ? o(m, v) : l.leftPad(m.toString(16), 64) + l.leftPad(v.toString(16), 64)
}

function p(t) {
    try {
        var n = m(function (e) {
            var t = {}
                , n = ["signData", "encData", "extra"];
            for (var i in e)
                e.hasOwnProperty(i) && !n.includes(i) && null != e[i] && (t[i] = e[i]);
            return t
        }(t.data));
        n.data = m(n.data);
        var i = function (e) {
            var t = [];
            for (var n in e)
                if (e.hasOwnProperty(n) && (e[n] || "".concat(e[n])))
                    if ("data" === n) {
                        var i = Object.assign({}, e[n]);
                        for (var r in i) {
                            if ("number" != typeof i[r] && "boolean" != typeof i[r] || (i[r] = "" + i[r]),
                            Array.isArray(i[r]) && !i[r].length && delete i[r],
                            Array.isArray(i[r]) && i[r].length > 0)
                                for (var o = 0; o < i[r].length; o++)
                                    i[r][o] = m(i[r][o]);
                            null != i[r] && i[r] || delete i[r]
                        }
                        var a = m(i);
                        t.push("".concat(n, "=").concat(JSON.stringify(a)))
                    } else
                        t.push("".concat(n, "=").concat(e[n]));
            return t.push("key=".concat(u)),
                t.join("&")
        }(n)
            , r = v(i, h, {
            hash: !0
        });
        return e.from(r, "hex").toString("base64")
    } catch (e) {
        console.log(e)
    }
}

function m(e) {
    var t = new Array
        , n = 0;
    for (var i in e)
        t[n] = i,
            n++;
    var r = [].concat(t).sort()
        , o = {};
    for (var a in r)
        o[r[a]] = e[r[a]];
    return o
}

u = "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P"
t = {}
t.data = {
    "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    "data": {
        "addr": "",
        "medinsLvCode": "",
        "medinsName": "北京医院",
        "medinsTypeCode": "",
        "pageNum": 1,
        "pageSize": 10,
        "regnCode": "110000",
        "sprtEcFlag": ""
    },
    "encType": "SM4",
    "signType": "SM2",
    "timestamp": 1637030853,
    "version": "1.0.0"
}
p(t)