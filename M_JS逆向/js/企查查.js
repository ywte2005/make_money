var codes = {
    0: 'W',
    1: 'l',
    2: 'k',
    3: 'B',
    4: 'Q',
    5: 'g',
    6: 'f',
    7: 'i',
    8: 'i',
    9: 'r',
    10: 'v',
    11: '6',
    12: 'A',
    13: 'K',
    14: 'N',
    15: 'k',
    16: '4',
    17: 'L',
    18: '1',
    19: '8'
}

function Sdefault(a) {
    for (var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/", e = t.toLowerCase(), a = e + e, n = "", s = 0; s < a.length / 2; ++s) {
        var o = a[s].charCodeAt() % 20;
        n += codes[o]
    }
    return n
}




a = '/api/sns/applicationlist/api/sns/applicationlist'
var Sdefault_a = Sdefault(a)
// var i = S_idefault(a,Sdefault_a)
console.log(Sdefault_a)
