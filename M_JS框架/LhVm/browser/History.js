var History = function History() { //构建函数
    throw new TypeError("Illeglal constructor")
};
lhvm.safefunction(History);
Object.defineProperties(History.prototype, {
    [Symbol.toStringTag]: {
        value: 'History',
        configurable: true
    }
});
history = {};
history.__proto__ = History.prototype
history = lhvm.proxy(history)