var Navigator = function Navigator() { //构建函数
    throw new TypeError("Illeglal constructor")
};
lhvm.safefunction(Navigator);
Object.defineProperties(Navigator.prototype, {
    [Symbol.toStringTag]: {
        value: 'Navigator',
        configurable: true
    }
});
navigator = {};
navigator.__proto__ = Navigator.prototype
navigator = lhvm.proxy(navigator)