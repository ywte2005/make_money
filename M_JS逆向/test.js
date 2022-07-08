d = function (t, n, e, r) {
    return function r() {
        var o, i, u, p = !1;
        if ((i = r.__fiber__) ? (i.callStack[i.depth].paused = !0,
            r.__fiber__ = null,
            o = r.__construct__,
            r.__construct__ = null) : (i = new s(e),
            p = !0),
            u = r.__callname__ || t.name,
            r.__callname__ = null,
            i.pushFrame(t, this, n, arguments, r, u, o),
            p)
            return i.run(),
                i.rv
    }
}
console.log(d())