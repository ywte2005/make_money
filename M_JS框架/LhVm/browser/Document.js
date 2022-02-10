var Document = function Document() { //构建函数

};
lhvm.safefunction(Document);
Object.defineProperties(Document.prototype, {
    [Symbol.toStringTag]: {
        value: 'Document',
        configurable: true
    }
});

document = {};
document.__proto__ = Document.prototype
document = lhvm.proxy(document)