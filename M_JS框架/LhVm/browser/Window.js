window = this;
var Window = function Window() {
    //容易被检测到的  堆栈
    throw new TypeError("Illegal constructor");
};
lhvm.safefunction(Window)

Object.defineProperties(Window.prototype, {
    [Symbol.toStringTag]: {
        value: 'Window',
        configurable: true
    }
});
//////////////////////////////////////
Window.prototype.PERSISTENT = 1;
Window.prototype.TEMPORARY = 0;
Window.prototype.__proto__ = WindowProperties.prototype;
//////////////////////////////////////
window.__proto__ = Window.prototype;
