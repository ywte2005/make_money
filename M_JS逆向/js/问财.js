const jsdom = require("jsdom");
const {
    JSDOM
} = jsdom;
const dom = new JSDOM(` < !DOCTYPE html > <p > Hello world < /p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;
global.navigator = {userAgent: 'node.js',};
var TOKEN_SERVER_TIME = 1634542998.979;
!function (n, t, r, e, a, u, c) {
    !function () {
        var s = a[0]
            , v = e[0]
            , f = u[0]
            , l = st(e[1], r[0])
            , d = a[1]
            , p = n[0]
            , h = a[2]
            , g = n[1]
            , w = a[2]
            , m = Zn(a[3], u[1], a[4])
            , I = a[5]
            , _ = r[1]
            , y = e[2]
            , E = a[6]
            , A = at(n[2], u[2], n[3], e[3])
            , C = u[3]
            , b = t[0]
            , B = a[7]
            , R = u[4]
            , k = u[5]
            , T = e[4]
            , O = Zn(a[8], a[9], c[0])
            , S = Zn(r[2], t[1], t[2], c[1])
            , x = n[4]
            , L = r[3]
            , M = e[5]
            , N = u[6]
            , P = st(e[6], a[10])
            , D = r[4]
            , j = Zn(r[5], a[11], t[3])
            , V = c[2]
            , W = e[7]
            , X = r[6]
            , $ = n[5]
            , F = st(u[7], a[12], a[13])
            , H = st(r[7], u[8], u[9])
            , Y = u[10]
            , U = c[3]
            , K = a[14]
            , z = c[4]
            , G = r[8]
            , Q = n[6]
            , Z = n[7]
            , J = u[11]
            , q = Gn(a[15], t[4])
            , nn = a[16]
            , tn = n[8]
            , rn = a[17]
            , en = r[9]
            , an = e[8]
            , on = Gn(u[12], r[10])
            , un = a[18]
            , cn = r[11]
            , sn = at(e[9], t[5], n[9])
            , vn = e[10]
            , fn = at(n[10], e[3], r[12])
            , ln = e[11]
            , dn = e[12]
            , pn = r[13]
            , hn = r[14]
            , gn = n[11]
            , wn = n[12]
            , mn = r[15]
            , In = n[13]
            , _n = e[13]
            , yn = r[16]
            , En = e[14]
            , An = e[15]
            , Cn = Gn(n[14])
            , bn = t[6]
            , Bn = a[19]
            , Rn = e[16]
            , kn = r[17]
            , Tn = c[5]
            , On = n[15]
            , Sn = Zn(n[16], t[7], n[17])
            , xn = st(t[8], u[13])
            , Ln = t[9]
            , Mn = e[17]
            , Nn = u[14]
            , Pn = r[3]
            , Dn = t[10]
            , jn = a[20]
            , Vn = at(c[6], t[11], c[7], t[12])
            , Wn = c[8]
            , Xn = c[9]
            , $n = u[15]
            , Fn = e[18]
            , Hn = e[18]
            , Yn = c[10]
            , Un = s + v
            , Kn = c[11]
            , zn = n[18];

        function Gn() {
            var e = arguments[r[18]];
            if (!e)
                return n[19];
            for (var o = t[13], i = a[21], u = n[18]; u < e.length; u++) {
                var s = e.charCodeAt(u)
                    , v = s ^ i;
                i = i * u % a[22] + c[12],
                    o += t[14].fromCharCode(v)
            }
            return o
        }

        function at() {
            var n = arguments[t[15]];
            if (!n)
                return a[53];
            for (var r = e[33], o = a[54], i = a[55], u = a[25]; u < n.length; u++) {
                var s = n.charCodeAt(u);
                i = (i + c[33]) % o.length,
                    s ^= o.charCodeAt(i),
                    r += a[3].fromCharCode(s)
            }
            return r
        }

        function st() {
            var t = arguments[c[33]];
            if (!t)
                return r[21];
            for (var e = n[19], o = a[21], i = r[18]; i < t.length; i++) {
                var u = t.charCodeAt(i)
                    , s = u ^ o;
                o = u,
                    e += r[82].fromCharCode(s)
            }
            return e
        }

        var Qn = [new a[23](n[20]), new e[3](f + l + d + p)];

        function Zn() {
            return arguments[t[15]].split(n[19]).reverse().join(t[13])
        }

        var Jn = [new t[16](c[13]), new u[9](e[19])],
            qn = a[24][u[16]] || a[24].getElementsByTagName(st(r[19], r[20]))[a[25]], nt;
        !function (o) {
            var i = n[21]
                , s = c[14]
                , v = at(e[20], n[22], n[23])
                , f = a[26];
            o[i + s] = n[24];

            function l() {
                var t = c[15];
                this.setCookie(t, a[27]),
                this.getCookie(t) || (o[u[17]] = n[25]),
                    this.delCookie(t)
            }

            o[c[16]] = l;

            function d(t, e, a) {
                var o, i, c;
                o = i = c = r;
                var s, f, l;
                s = f = l = n;
                var d, p, h;
                d = p = h = u;
                var g = Gn(p[18], f[26]);
                this.setCookie(t, o[21], v + g, e, a)
            }

            o[n[27]] = p;

            function p(r) {
                var a = t[17][e[21]]
                    , o = f + h + r + t[18]
                    , i = a.indexOf(o);
                if (i == -n[28]) {
                    if (o = r + n[29],
                    a.substr(e[22], o.length) != o)
                        return;
                    i = u[19]
                }
                var s = i + o[c[17]]
                    , v = a.indexOf(g + w, s);
                return v == -e[23] && (v = a[n[30]]),
                    a.substring(s, v)
            }

            o[e[24]] = m;

            function m(e, o, i, u, s) {
                var v = e + c[18] + o;
                u && (v += n[31] + u),
                s && (v += Zn(t[19], a[28], n[32], c[19]) + s),
                i && (v += r[22] + i),
                    c[20][c[21]] = v
            }

            o[a[29]] = d
            var i = a[45]
                , s = e[15]
                , v = Gn(u[27], jn)
                , l = Zn(c[29], a[46], e[30], t[27])
                , d = t[28]
                , p = a[47]
                , h = n[42]
                , g = n[43]
                , w = c[11];

            function m(o) {
                for (var s = Zn(sn, nn, n[44]), v = u[19], f = o[c[17]], l = []; v < f;) {
                    var d = A[o.charAt(v++)] << parseInt(C + s, r[26]) | A[o.charAt(v++)] << parseInt(r[27], c[30]) | A[o.charAt(v++)] << a[48] | A[o.charAt(v++)];
                    l.push(d >> parseInt(a[49], c[31]), d >> u[28] & parseInt(Gn(e[31]), t[15]), d & parseInt(i + b, r[28]))
                }
                return l
            }

            function I(e) {
                var a = (L,
                    _,
                    m(e));
                if (a[c[26]] != w)
                    return error = u[29],
                        void 0;
                var o = a[n[28]]
                    , i = [];
                return S(a, +r[29], i, +t[25], o),
                    x(i) == o ? i : void 0
            }

            for (var y = Zn(Jn, r[30], a[50]), A = {}, O = r[18]; O < parseInt(B + s + R, c[31]); O++)
                A[y.charAt(O)] = O;

            function S(n, e, a, o, i) {
                for (var c = n[u[23]]; e < c;)
                    a[o++] = n[e++] ^ i & parseInt(st(f, u[24], E), t[29]),
                        i = ~(i * parseInt(Gn(u[30]), r[29]))
            }

            function x(t) {
                for (var r = n[45], e = c[26], o = n[18], i = t[n[30]]; o < i; o++)
                    e = (e << u[31]) - e + t[o];
                return e & parseInt(v + r, a[44])
            }

            function L(n) {
                var t = x(n)
                    , e = [w, t];

                return S(n, +c[26], e, +r[29], t), M(e)
            };
            var lyb =[142, 146, 196, 5, 97, 109, 47, 238, 97, 109, 55, 63, 95, 205, 85, 143, 7, 10, 5, 0, 0, 188, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 14, 164, 0, 0, 0, 0, 0, 0, 0, 19, 3]
            window.ly=L(lyb)

            function M(o) {
                for (var i = t[28], s = n[18], v = o[r[31]], f = []; s < v;) {
                    var p = o[s++] << parseInt(at(n[46], c[32], t[30]), r[28]) | o[s++] << parseInt(u[32], c[31]) | o[s++];
                    f.push(y.charAt(p >> parseInt(e[32], a[11])), y.charAt(p >> parseInt(t[31], c[28]) & parseInt(k + l, n[47])), y.charAt(p >> a[48] & parseInt(i + d, n[40])), y.charAt(p & parseInt(a[51], a[52])))
                }
                return f.join(t[13])
            }
        }(nt || (nt = {}));

    }()
}([".", ";", Array, "L_", "bo", "oByt", "get", "Key", "os", "uV&", "!O", "ro", "2345Ex", "we", "\u2552\u0973\u095f\u09e3", "e", "=:", "f", 0, "", "thsi.cn", "all", 86, "l_#\x19\x18\x07g\x15rV8\x15\t\x0ea", !0, !1, "'Vd$;", "getCookie", 1, "=", "length", "; domain=", "=htap ;", RegExp, "___", "body", "documentElement", "F[)", "reffuBot", ".c\x1e", 8, "decodeBuffer", "e64", "ode", "2", "7", "\\S[", 16, "scr", "ng", "l?+", "124f80", "readyState", "\u255f\u096f\u095f\u09f7", "1002", "1750", "on", 2, "le", "i", "\x02", "timeNow", "\u2554\u0975\u0957", "wheel", "click", "BIDUBr", document, window, "tcejbOXevitcA", "Weak", "Apple Computer, Inc.", 'yT"\\NR\x0ezZ]3VL', "&o&6d", "RESWORBBL", "chr", 53, "Q", "\u2544\u0964\u0949\u09e5\u09b5\u0930\u09a2\u09d0\u099a\u09da\u09b7\u09d0\u09df\u09d8", "Ldz]", "^MacIntel", '_R"wJX!F]E\x10PYC#G]', "\u2506\u092d", "s", "or", "ej", "gm", "hY*%_", "^https?\\:", 33, "host", "\\.?", "g", "analys", "isRst", "headers", "prototype", "CHAM", "ADED", 51], ["5", Object, "cot", '"^', "@s", "O7N", "getAll", "pbE(\x1b", Boolean, "h", "ELEO", "&]^", 71, "", String, 2, RegExp, document, "=", " P", "$&", '<script>document.w=window<\/script><iframe src="/favicon.icon"></iframe>', "frames", 79, "Init", 0, ",x", 82, "7", 10, "\t\x01", "12", "W[", 7, "onerror", 85, "ti", Date, "\u255b\u0978\u0954", / /g, 1, "TR8RL_", "[@:]", "getServerTime", "y7", "\x17[\x16->", ".", "ckP", !0, "isTrusted", "R\x1d", window, "ActiveXObject", "vendor", "i", "\u255e", "ch", "navigator", "length", 50, "savnac", "name", "1", "H\x1e/", "\x1e ", 16, "ShockwaveFlash.ShockwaveFlash", 95, "\u2569\u253e\u2557\u2539\u250a\u2538", 15, "21", "vent", "List", "et", "Respon", "]E$", !1, "^_self$", "KE5pTR;PVC", "A", "\u2576\u097e\u094e\u09f8\u09a6\u0938\u09b6\u09fe\u0996\u09d7\u09a7\u09d2\u09cc", 26, "\u2569", "jsonp_ignore", "\u2508"], ["\u2556\u253f", "ume", 29, "lo", '"$', "*`or", "strT", Date, "sted", "vent", "D:jt", "ect", "_[3", "owser", "chr", "plug", "iso", "get", 0, "bt39M", "\u255f\u253a\u255b\u253f", "", "; expires=", 28, "[!\"#$%&'()*+,/\\\\:;<=>?@[\\]^`{|}~]", "htmlfile", 8, "1100", 10, 2, "tV", "length", "encode", 92, "11111010000", "readyState", document, "ire", "url", "object", "href", 16, "gth", 1, "\u251b", ":", "10", RegExp, "\u2569\u0966\u0914\u09bb\u09ad\u0979", "i$G$", 5, "^(\\d+\\.)+\\d+$", "kal", "analysisRst", "getOriginFromUrl", "addEventListener", 3, "onwheel", "getMouseWhell", "ome", window, "head", "egasseMtsop", 'HN"]WY', "sgAppName", "Maxthon", 71, "UBrowser", "i", "MSGesture", 30, "J\x1a0", "platform", "\x16~4x", "language", "^iPad", "^iPod", "getBrowserIndex", "11", "16", 4, "update", String, "addE", "011", "\u2519", "Z|A", " 00:00:0", "seHead", "110", 27, "Cl", "target", "parentNode", "unload", "&;", "locotorp", "\u2544\u2536\u2555", "\u2507\u093d\u097d\u09dc\u0984", "\u2556\u0971\u0956\u09fe\u09a7", "headers", 81, "PR7Q]E%", 77, "Y[", "&"], ["er-Message", Boolean, "e_f", RegExp, "Enc", "on", Array, "th", "Uint", "\x1e~)", "Goo", "c.", "me", "l2", "-88", "0", "e", "_r", "hexin-v", "so.thsi.cn", 20, "cookie", 0, 1, "setCookie", "localStorage", "head", !1, "le", "prototype", "f", "\u2506\u092c\u090b\u09a0\u09e1\u096c\u09df\u0980", "10010", "", "#\x1aA}t", "readyState", "onload", 96, null, "status_code", 10, "undefined", "length", "Ogd[", 2, "\u2550\u0978\u094e\u09d9\u09bf\u092e\u099a\u09f7\u0986\u09d2\u09af\u09e4\u09ca\u09d1", "onmousewheel", document, "getMouseMove", "getMouseClick", "^Linux ", "8*'", "\u2554\u2535\u2559\u2535\u2565\u250d\u256c\u2502\u2576\u2519\u2574", "tingsE", "\x16Gb", "\u2560\u0978\u095b\u09fa\u099d\u093c\u099e", "vitcA", "MY5", window, "k:", "opr", "W(Nv", "plorer", "aef", "revirdbew", "\\X\x18ZLc$T[\\", "xK}", "TR8RL_", "ontouchstart", "dy", Date, "ActiveXObject", "Shockwave", "\u2569\u095c\u0968\u09dc", "getPluginNum", 7, 8, 9, "ers", 'f\x1fx\x1f\x07\x1eln\x18k"h\x12\x1f\rkdE\n[e\x1d\x7fiJ\br', "error", "LV", !0, "click", "tagName", "emantsoh", "insertBefore", '\\y$g"', "w", "\\?", encodeURIComponent, "Init"], ["X-Antispid", "du", " ", String, "___", "duc", "ile", "1", 'Ez@"', '"rQ@X', "\u2554\u2520\u257f", 2, "\u2552\u2521", 47, "tou", "\u2559", "Cli", "MozSet", "eXObj", "b", "ELEO", 9527, 256, RegExp, document, 0, ";", !0, 33, "delCookie", window, 74, "\\X5@UR8A", "\u2550", "addBehavior", "&d?\x1ep", "set", "#default#userData", "del", "ng", "ZV%", "ds", "base_fileds", 71, 8, "25", 78, "bas", 6, "20", "_-9876543210zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA", "3f", 16, "", "V587", 2333, "event", "pro", "\x1c0i]", "src", "//s.thsi.cn/js/chameleon/time.1", 1, "WY:ZYS", "onreadystatechange", "1111101001", "location", "i", "3", Date, "\x16\x1d", "length", "\u2569\u0941\u0949\u09bb\u09f8\u0962\u09d4\u09d9\u0980\u09c9\u09b2\u09c2\u0987\u0987\u099f\u0a2e\u0a40\u09f2\u09b1\u0963\u090c\u09e0\u09d6\u09aa\u099a\u0921\u097d\u092d\u0a37\u09a1\u09e5\u090d\u09b0\u09c0\u0971\u0a38", "booleanToDecimal", "\u2550\u2535\u2541", "DOMMouseScroll", "\u255a\u2535\u2540\u2533\u2556\u253b\u2554\u2522\u2547", "isTru", "clientY", "ro", "[ix]\\d+", "maxHeight", "ActiveXObject", "ay", "vendor", "QQBrowser", "0`L", 12, !1, "th", "plugins", "PDF|Acrobat", "localStorage", "Native Client", "TV8RMV1PK", "10000", "^Win64", "^Linux armv|Android", "getPlatform", 36, "\b", 5, 10, "16", "10", 3, "Init", "h", 35, "tar", "Gg", 44, 84, "\\", ")`7\x1e", "11", "\u2564\u2527\u2575\u253c\u256c\u2538", "\u2544\u2536\u2555", "appendChild", "_str", "C[Q\x1f", 98, "=", "CHAM"], [".b", 73, Array, "2", "0", "3", "red", Error, "\u2576\u2512\u2576\u2504", RegExp, "Bind", "Dow", "\u250f\u095c\u0948\u09e3", "\u2544", "aw", "v", "head", "allow", "\u2507\u093d\u090a\u09a1\u09ea\u096d\u09de\u098b\u09c4\u098d\u09e2\u09f6\u09f5\u09e9", 0, "\\^ ", window, 1, "length", "\u2505\u2530\u2505", 49, "base_fileds", "\u2504\u092a", 8, "error", "\u2506\u092d\u090a\u09a1\u09e0\u096d\u09df\u0980", 5, "10", "base64Decode", "\x16C", "edoced", "dy", '^"', "isIP", 16, ".js", "loaded", 13, 'WY$PYS/FLV"P[_7[_R', "^\\s*(?:(https?:))?\\/{2,}([^\\/\\?\\#\\\\]+)", "8", "", "@", "parse", "JV8QWZ", "serverTimeNow", "mousewheel", document, "ch", "em", "le", "safari", "U`N", "ActiveXObject", " In", "i", "\u2554\u0975\u0948\u09fe\u09bd\u0938", "chrome", "bg", "defaultCharset", "1e0", "zh-cn", "}Y6n", "^BlackBerry", "110", 10, "010", "V\x17^", "th", "open", "a", "rg", "submit", "XMLHTTP", "#", 36, 2, "M]J", "/s", "ng", "Window", "N_LO"], ["tpi", "=sB4", ".*", "d", "ove", "r", Boolean, "vh\x1az", "ADED", !0, "CHAMELEON_CALLBACK", 3, 2333, "s.thsi.cn", "ow", "checkcookie", "Init", "length", "=", "Nq", document, "cookie", "nt", RegExp, "^d", "documentElement", 0, 48, 10, "8ixl", 2, 8, 5, 1, '"$', Date, "complete", "interactive", "ca", "\u2506\u092c\u090b\u09a0\u09e1\u096d\u09df\u0981\u09c4\u098d", "redirect_url", "\u2552", 49, "\u250d", "W\x15G\x168", "\u2506\u092c\u090b\u09a0\u09e1\u096c\u09df\u0980\u09c5\u098c\u09f3\u0980\u0989\u098c\u0987\u0a20\u0a2d\u09ec\u09fb\u0960\u0911\u09ac\u09cf\u09c0\u09f5\u094c\u0963\u0940\u0a39\u09cc\u09f7\u0960", "strhash", "getRootDomain", "\\.com\\.cn$|\\.com\\.hk$", 45, ".", "v", 44, "keydown", "clientX", "ins", window, "u!", "chrome", "\x1f=", "ome", "TheWorld", "\u2554\u0975\u0948\u09fe\u09bd\u0938", 30, 'UD\x12ZvX"aJV5^', "plugins", ":0A8h", !1, "\u2502\u0924\u0917", 93, "\u2569\u095c\u0954\u09f5\u09a2\u0932\u0987\u09d5", "^iPhone", "13", "3c", "Fri, 01 ", "Feb 2050", "a", "i", "#", 20, "error", "\\.", "$", "apply", 69, "/", "\u256f\u2522\u256e\u2526\u2552\u2526\u2556\u2504\u2561\u2510\u2565\u2500\u2573\u2507", "fetch", "headers", 71, "0000021"]);
console.log(window.ly)
