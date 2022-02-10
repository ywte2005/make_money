function r(t) {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "-"
        , n = (Math.random().toString(16) + "000000000").substr(2, 8);
    return t ? e + n.substr(0, 4) + e + n.substr(4, 4) : n
}

function getSignKey () {
    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "-";
    return r(!1, t) + r(!0, t) + r(!0, t) + r(!1, t)
}

console.log(getSignKey())


