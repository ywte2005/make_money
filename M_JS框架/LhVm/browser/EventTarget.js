var EventTarget = function EventTarget() { //构造函数

};
lhvm.safefunction(EventTarget)

Object.defineProperties(EventTarget.prototype, {
    [Symbol.toStringTag]: {
        value: 'EventTarget',
        configurable: true
    }
});
EventTarget.prototype.addEventListener = function addEventListener() {
    debugger
};
lhvm.safefunction(EventTarget.prototype.addEventListener)

EventTarget.prototype.dispatchEvent = function dispatchEvent() {
    debugger
};
lhvm.safefunction(EventTarget.prototype.dispatchEvent)


EventTarget.prototype.removeEventListener = function removeEventListener() {
    debugger
};
lhvm.safefunction(EventTarget.prototype.removeEventListener)