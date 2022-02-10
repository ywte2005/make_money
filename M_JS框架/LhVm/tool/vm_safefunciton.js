(() => {
    "use strict";
    const $toString = Function.toString;
    const myFunciton_toString_symbol = Symbol("(".concat('', ")_", (Math.random() + "").toString(36)));
    const myToString = function () {
        return typeof this == "function" && this[myFunciton_toString_symbol] || $toString.call(this);
    };

    function set_native(func, key, value) {
        Object.defineProperty(func, key, {
            "enumerable": false,
            "configurable": true,
            "writable": true,
            "value": value
        })
    }

    delete Function.prototype["toString"];//删除原型链上的toString
    set_native(Function.prototype, "toString", myToString); // 自己定义一个getter方法
    set_native(Function.prototype.toString, myFunciton_toString_symbol, "function toString() { [native code] }"); //套娃保护toString
    this.lhvm.safefunction = (func) => {
        set_native(func, myFunciton_toString_symbol, `function ${myFunciton_toString_symbol, func.name || ""}() { [native code] }`);
    };
}).call(this);