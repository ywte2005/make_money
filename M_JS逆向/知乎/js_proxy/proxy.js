let _stringify = JSON.stringify;
JSON.stringify = function (Object) {
    // ?? 的意思是，如果 ?? 左边的值是 null 或者 undefined，那么就返回右边的值。
    if ((Object?.value ?? Object) === global) {
        return "global";
    }
    return _stringify(Object);
};

function getMethodHandler(WatchName) {
    let methodhandler = {
        apply(target, thisArg, argArray) {
            let result = Reflect.apply(target, thisArg, argArray);
            console.log(`[${WatchName}] apply function name is [${target.name}], argArray is [${argArray}], result is [${result}].`);
            return result;
        },
        construct(target, argArray, newTarget) {
            let result = Reflect.construct(target, argArray, newTarget);
            console.log(`[${WatchName}] construct function name is [${target.name}], argArray is [${argArray}], result is [${JSON.stringify(result)}].`);
            return result;
        }
    };
    return methodhandler;
}

function getObjHandler(WatchName) {
    let handler = {
        get(target, propKey, receiver) {
            let result = Reflect.get(target, propKey, receiver);
            if (result instanceof Object) {
                if (typeof result === "function") {
                    console.log(`[${WatchName}] getting propKey is [${propKey}] , it is function`);
                    //return new Proxy(result,getMethodHandler(WatchName))
                } else {
                    console.log(`[${WatchName}] getting propKey is [${propKey}], result is [${JSON.stringify(result)}]`);
                }
                return new Proxy(result, getObjHandler(`${WatchName}.${propKey}`));
            }
            console.log(`[${WatchName}] getting propKey is [${propKey}], result is [${result}]`);
            return result;
        },
        set(target, propKey, value, receiver) {
            if (value instanceof Object) {
                console.log(`[${WatchName}] setting propKey is [${propKey}], value is [${JSON.stringify(value)}]`);
            } else {
                console.log(`[${WatchName}] setting propKey is [${propKey}], value is [${value}]`);
            }
            return Reflect.set(target, propKey, value, receiver);
        },
        has(target, propKey) {
            let result = Reflect.has(target, propKey);
            console.log(`[${WatchName}] has propKey [${propKey}], result is [${result}]`);
            return result;
        },
        deleteProperty(target, propKey) {
            let result = Reflect.deleteProperty(target, propKey);
            console.log(`[${WatchName}] delete propKey [${propKey}], result is [${result}]`);
            return result;
        },
        getOwnPropertyDescriptor(target, propKey) {
            let result = Reflect.getOwnPropertyDescriptor(target, propKey);
            console.log(`[${WatchName}] getOwnPropertyDescriptor  propKey [${propKey}] result is [${JSON.stringify(result)}]`);
            return result;
        },
        defineProperty(target, propKey, attributes) {
            let result = Reflect.defineProperty(target, propKey, attributes);
            console.log(`[${WatchName}] defineProperty propKey [${propKey}] attributes is [${JSON.stringify(attributes)}], result is [${result}]`);
            return result;
        },
        getPrototypeOf(target) {
            let result = Reflect.getPrototypeOf(target);
            console.log(`[${WatchName}] getPrototypeOf result is [${JSON.stringify(result)}]`);
            return result;
        },
        setPrototypeOf(target, proto) {
            console.log(`[${WatchName}] setPrototypeOf proto is [${JSON.stringify(proto)}]`);
            return Reflect.setPrototypeOf(target, proto);
        },
        preventExtensions(target) {
            console.log(`[${WatchName}] preventExtensions`);
            return Reflect.preventExtensions(target);
        },
        isExtensible(target) {
            let result = Reflect.isExtensible(target);
            console.log(`[${WatchName}] isExtensible, result is [${result}]`);
            return result;
        },
        ownKeys(target) {
            let result = Reflect.ownKeys(target);
            console.log(`[${WatchName}] invoke ownKeys, result is [${JSON.stringify(result)}]`);
            return result;
        },
        apply(target, thisArg, argArray) {
            let result = Reflect.apply(target, thisArg, argArray);
            console.log(`[${WatchName}] apply function name is [${target.name}], argArray is [${argArray}], result is [${result}].`);
            return result;
        },
        construct(target, argArray, newTarget) {
            let result = Reflect.construct(target, argArray, newTarget);
            console.log(`[${WatchName}] construct function name is [${target.name}], argArray is [${argArray}], result is [${JSON.stringify(result)}].`);
            return result;
        }
    };
    return handler;
}
let _window = {
    XMLHttpRequest: function (){},
    sessionStorage: function (){},
    localStorage: function (){},
};
let _navigator = {
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
    appCodeName: "Mozilla",
    plugins: {
        length: 0
    },
    toString: function (){
        return "[object Navigator]";
    }
};
let _screen = {
    colorDepth: 24,
    height: 900,
    width: 1440,
};
_screen.toString=function () {
    return '[object Screen]';
};
var _Document = function Document() { //构造函数

};


Object.defineProperties(_Document.prototype, {
    [Symbol.toStringTag]: {
        value: "Document",
        configurable: true
    }
})
function mu_() {
    var e = [];
    var a = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (var b = 0; b < 28; b++) {
        e[b] = a[Math.floor(Math.random() * a.length)]
    }
    ;return e.join('')
}
var CanvasRenderingContext2D_ = {
    toString: function() {
        return "[object CanvasRenderingContext2D]"
    }
};
CanvasRenderingContext2D_.__proto__.fillText = function fillText() {}
;
CanvasRenderingContext2D_.__proto__.arc = function arc() {}
;
CanvasRenderingContext2D_.__proto__.stroke = function stroke() {}
;
var getContext_ = {
    toString: function() {
        return "[object WebGLRenderingContext]"
    }
};
var aaaaa=0;
var canvas = {
    toDataURL: function toDataURL() {
        return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAQCAYAAABQrvyxAAACN0lEQVRIS8WWP0hWYRTGf98S5NBSm5sObgWt6RJR5uLQIGRC1OAWNEspOAWCIIR+4GYFDg1NEoEQ5tIghFNbBIlDLi5Bi/LIOXA8vu/1Q76v7nLvff+c9zzPc55zb4vT11F612vLxjTnz4Vl/3xoCHhaSsgTzQlncL0EcxV4C9xLtLSB58Af4AyAEvu+Pyf7P9S4BdwG5i2pogIl1mMJRUJ6qUCux8vAIvAeeABM24J2idm8ueaBCHYSmDJ2XgLPgO+Axt8AGnPmFF/srQM3PJFQGiUzKc5AIcYZDzQpoMAlH0jaLyGRHeAmsAI8BN4BrwIor28B2gac3S2r+wxAyY8YwL7kjaICnTCe2Rc7m3ay6rQfOAQ+AL+BpQAgAnZlYpIyqC4HKpBRPQfYaGKBcLbjs7fVOOcHaU4HvQZmgfvADHAtAfASiqAygBeAgGr8oNKgiwA82Xj30inNzVlwv+tQHb4MXDdAOigmqy2+zhMsKRCZjn7x8Ucqp2jiWhvNCkRCZNDPwKoNemI/gDWr8Qjgp3UTdZGPgeEagAzUz3bf/DqvFTb1e83tA6PAtwBAho7JRQBaNgZ8NaXOU0BqylvyQb4Ud66mQKce+ATcDZHdoLFt1hQ4KQHb26SAPDVhbblRgfwLEdkvzYn9J8BGxWTdGs7fDI87LGWyAtmosev43BVrkT7XrUQvFKfkgUvA30o0Sb0A6KfKO8+FDu7WphKAceCxfYD27Hsw" + mu_() + "AAAAAElFTkSuQmCC"
    },
    getContext: function getContext(x) {
        if (x === "2d") {
            return CanvasRenderingContext2D_
        } else {
            return getContext_
        }
    }
};
canvas[Symbol.toStringTag] = "HTMLCanvasElement";
canvas.getContext[Symbol.toStringTag] = "WebGLRenderingContext";
_document = {
    createElement: function createElement(x) {
        return canvas
    },
    getElementById: function getElementById(x) {
        debugger
        return null
    },
    getElementsByClassName: function getElementsByClassName(x) {
        return []
    }
};
_document.__proto__ = _Document.prototype;
_document.getElementById.__proto__=function () { return "[native code]" }
_document.toString=function () {
    return "[object HTMLDocument]";
};
let _location={
    "href": "https://www.zhihu.com/",
    "host": "www.zhihu.com",
    "hostname": "www.zhihu.com",
    "pathname": "/",
    "port": "",
    "protocol": "https:",
    "search": "",
    "hash": "",
    "origin": "https://www.zhihu.com",
    "assign": function (url) {
        this.href = url;
    }
}
_location.toString=function () {
    return "https://www.zhihu.com/question/waiting";
};
let _history={

}
_history.toString=function () {
    return '[object History]';
};
_Document={}
_Document.toString=function () {
    return "[native code]";
};
// _window = Object.assign(global, _window);
const window = new Proxy(Object.create(_window), getObjHandler("window"));
const navigator = new Proxy(Object.create(_navigator), getObjHandler("navigator"));
const screen = new Proxy(Object.create(_screen), getObjHandler("screen"));
const location = new Proxy(Object.create(_location), getObjHandler("location"));
const document = new Proxy(Object.create(_document), getObjHandler("document"));
const history = new Proxy(Object.create(_history), getObjHandler("history"));
const Document = new Proxy(Object.create(_Document), getObjHandler("history"));
module.exports = {
    window,
    navigator,
    screen,
    location,
    document,
    history,
    Document
};