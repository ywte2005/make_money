function ia() {
    return function () {
        var t = e(6, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            , n = e(1, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            , i = e(1, "0123456789");
        return n + i + t
    }();

    function e(e, t) {
        e = e || 32;
        for (var n = "", i = 0; i < e; i++)
            n += t.charAt(Math.ceil(1e3 * Math.random()) % t.length);
        return n
    }
}

var r = Math.ceil((new Date).getTime() / 1e3)
    , o = ia()
    , a = r + o + r;

console.log(a)