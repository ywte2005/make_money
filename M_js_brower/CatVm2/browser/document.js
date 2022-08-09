var Document = function Document() { //构造函数

};
catvm.safefunction(Document);


Object.defineProperties(Document.prototype, {
    [Symbol.toStringTag]: {
        value: "Document",
        configurable: true
    }
})
document = {};
document.__proto__ = Document.prototype;
document.referer = location.href || "";
//////////////////////////////////////////////////////////
document.cookie = "_zap=e2037bb2-72f1-4c22-bef5-28fa54ba5518; d_c0=\"ACDdD0QhwxOPTswPx4x9ypoP7A76ZTx6Tk0=|1632292463\"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1659690149; _xsrf=fc64a6a9-c6b6-47fd-9e4f-1c05e705fab0; KLBRSID=b4f9781e1155b8a1bc876ec55da1029a|1659690237|1659690148; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1659690237; SESSIONID=Q7glVdIIQjSoGFQQ4F354A9XyKizgTt8T2gW6KPyQu7; JOID=U1kQB04Fn58ZW9F-SQCLS58f9bleVKz5dAm1MwFQ9ch3HZMvHKRGc35f1XtJcusz3l_dQ3HQ0nqmgKiy4lkFU1Q=; osd=Ul8XB00EmZgZWNB4TgCISpkY9bpfUqv5dwizNAFT9M5wHZAuGqNGcH9Z0ntKc-003lzcRXbQ0Xugh6ix418CU1c=";
document.getElementById = function getElementById(id) {
    debugger;
    //用id 匹配当前环境内存已有的元素
    return null;

};
catvm.safefunction(document.getElementById)


document.addEventListener = function addEventListener() {

};
catvm.safefunction(document.addEventListener)



document.createElement = function createElement(tagName) {
    var tagname = tagName.toLowerCase() + "";
    if (catvm.memory.htmlelements[tagName] != undefined) {
        debugger;
    }
    return catvm.proxy(catvm.memory.htmlelements[tagName]())

};
catvm.safefunction(document.createElement)


//////////////////////////////////////////////////////////

document = catvm.proxy(document);