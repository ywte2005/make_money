var Screen = function Screen() { //构建函数
    throw new TypeError("Illeglal constructor")
};
lhvm.safefunction(Screen);
Object.defineProperties(Screen.prototype, {
    [Symbol.toStringTag]: {
        value: 'Screen',
        configurable: true
    }
});
/////////////////////////////////////////
Screen.prototype.availHeight = 1040
/////////////////////////////////////////
screen = {};
screen.__proto__ = Screen.prototype
screen = lhvm.proxy(screen)