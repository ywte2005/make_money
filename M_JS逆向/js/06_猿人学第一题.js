const jsdom = require("jsdom")
const {JSDOM} = jsdom
const dom = new JSDOM("< !DOCTYPE html > <p > Hello world < /p>")
window = dom.window
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;
// w();
// dd();
function oo0O0(mw) {
    window.b = '';
    var U = ['W5r5W6VdIHZcT8kU', 'WQ8CWRaxWQirAW=='];
    var J = function (o, E) {
        o = o - 0x0;
        var N = U[o];
        if (J['bSSGte'] === undefined) {
            var Y = function (w) {
                var m = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=',
                    T = String(w)['replace'](/=+$/, '');
                var A = '';
                for (var C = 0x0, b, W, l = 0x0; W = T['charAt'](l++); ~W && (b = C % 0x4 ? b * 0x40 + W : W, C++
                        %
                        0x4) ? A += String['fromCharCode'](0xff & b >> (-0x2 * C & 0x6)) : 0x0) {
                    W = m['indexOf'](W)
                }
                return A
            };
            var t = function (w, m) {
                var T = [],
                    A = 0x0,
                    C, b = '',
                    W = '';
                w = Y(w);
                for (var R = 0x0, v = w['length']; R < v; R++) {
                    W += '%' + ('00' + w['charCodeAt'](R)['toString'](0x10))['slice'](-0x2)
                }
                w = decodeURIComponent(W);
                var l;
                for (l = 0x0; l < 0x100; l++) {
                    T[l] = l
                }
                for (l = 0x0; l < 0x100; l++) {
                    A = (A + T[l] + m['charCodeAt'](l % m['length'])) % 0x100, C = T[l], T[l] = T[A], T[A] = C
                }
                l = 0x0, A = 0x0;
                for (var L = 0x0; L < w['length']; L++) {
                    l = (l + 0x1) % 0x100, A = (A + T[l]) % 0x100, C = T[l], T[l] = T[A], T[A] = C, b += String[
                        'fromCharCode'](w['charCodeAt'](L) ^ T[(T[l] + T[A]) % 0x100])
                }
                return b
            };
            J['luAabU'] = t, J['qlVPZg'] = {}, J['bSSGte'] = !![]
        }
        var H = J['qlVPZg'][o];
        return H === undefined ? (J['TUDBIJ'] === undefined && (J['TUDBIJ'] = !![]), N = J['luAabU'](N, E), J[
            'qlVPZg'][o] = N) : N = H, N
    };
    window['b']='dmFyIGhleGNhc2U9MDt2YXIgYjY0cGFkPSIiO3ZhciBjaHJzej0xNjtmdW5jdGlvbiBoZXhfbWQ1KGEpe3JldHVybiBiaW5sMmhleChjb3JlX21kNShzdHIyYmlubChhKSxhLmxlbmd0aCpjaHJzeikpfWZ1bmN0aW9uIGI2NF9tZDUoYSl7cmV0dXJuIGJpbmwyYjY0KGNvcmVfbWQ1KHN0cjJiaW5sKGEpLGEubGVuZ3RoKmNocnN6KSl9ZnVuY3Rpb24gc3RyX21kNShhKXtyZXR1cm4gYmlubDJzdHIoY29yZV9tZDUoc3RyMmJpbmwoYSksYS5sZW5ndGgqY2hyc3opKX1mdW5jdGlvbiBoZXhfaG1hY19tZDUoYSxiKXtyZXR1cm4gYmlubDJoZXgoY29yZV9obWFjX21kNShhLGIpKX1mdW5jdGlvbiBiNjRfaG1hY19tZDUoYSxiKXtyZXR1cm4gYmlubDJiNjQoY29yZV9obWFjX21kNShhLGIpKX1mdW5jdGlvbiBzdHJfaG1hY19tZDUoYSxiKXtyZXR1cm4gYmlubDJzdHIoY29yZV9obWFjX21kNShhLGIpKX1mdW5jdGlvbiBtZDVfdm1fdGVzdCgpe3JldHVybiBoZXhfbWQ1KCJhYmMiKT09IjkwMDE1MDk4M2NkMjRmYjBkNjk2M2Y3ZDI4ZTE3ZjcyIn1mdW5jdGlvbiBjb3JlX21kNShwLGspe3Bbaz4+NV18PTEyODw8KChrKSUzMik7cFsoKChrKzY0KT4+PjkpPDw0KSsxNF09azt2YXIgbz0xNzMyNTg0MTkzO3ZhciBuPS0yNzE3MzM4Nzk7dmFyIG09LTE3MzI1ODQxOTQ7dmFyIGw9MjcxNzMzODc4O2Zvcih2YXIgZz0wO2c8cC5sZW5ndGg7Zys9MTYpe3ZhciBqPW87dmFyIGg9bjt2YXIgZj1tO3ZhciBlPWw7bz1tZDVfZmYobyxuLG0sbCxwW2crMF0sNywtNjgwOTc2OTM2KTtsPW1kNV9mZihsLG8sbixtLHBbZysxXSwxMiwtMzg5NTY0NTg2KTttPW1kNV9mZihtLGwsbyxuLHBbZysyXSwxNyw2MDYxMDU4MTkpO249bWQ1X2ZmKG4sbSxsLG8scFtnKzNdLDIyLC0xMDQ0NTI1MzMwKTtvPW1kNV9mZihvLG4sbSxsLHBbZys0XSw3LC0xNzY0MTg4OTcpO2w9bWQ1X2ZmKGwsbyxuLG0scFtnKzVdLDEyLDEyMDAwODA0MjYpO209bWQ1X2ZmKG0sbCxvLG4scFtnKzZdLDE3LC0xNDczMjMxMzQxKTtuPW1kNV9mZihuLG0sbCxvLHBbZys3XSwyMiwtNDU3MDU5ODMpO289bWQ1X2ZmKG8sbixtLGwscFtnKzhdLDcsMTc3MDAzNTQxNik7bD1tZDVfZmYobCxvLG4sbSxwW2crOV0sMTIsLTE5NTg0MTQ0MTcpO209bWQ1X2ZmKG0sbCxvLG4scFtnKzEwXSwxNywtNDIwNjMpO249bWQ1X2ZmKG4sbSxsLG8scFtnKzExXSwyMiwtMTk5MDQwNDE2Mik7bz1tZDVfZmYobyxuLG0sbCxwW2crMTJdLDcsMTgwNDY2MDY4Mik7bD1tZDVfZmYobCxvLG4sbSxwW2crMTNdLDEyLC00MDM0MTEwMSk7bT1tZDVfZmYobSxsLG8sbixwW2crMTRdLDE3LC0xNTAyMDAyMjkwKTtuPW1kNV9mZihuLG0sbCxvLHBbZysxNV0sMjIsMTIzNjUzNTMyOSk7bz1tZDVfZ2cobyxuLG0sbCxwW2crMV0sNSwtMTY1Nzk2NTEwKTtsPW1kNV9nZyhsLG8sbixtLHBbZys2XSw5LC0xMDY5NTAxNjMyKTttPW1kNV9nZyhtLGwsbyxuLHBbZysxMV0sMTQsNjQzNzE3NzEzKTtuPW1kNV9nZyhuLG0sbCxvLHBbZyswXSwyMCwtMzczODk3MzAyKTtvPW1kNV9nZyhvLG4sbSxsLHBbZys1XSw1LC03MDE1NTg2OTEpO2w9bWQ1X2dnKGwsbyxuLG0scFtnKzEwXSw5LDM4MDE2MDgzKTttPW1kNV9nZyhtLGwsbyxuLHBbZysxNV0sMTQsLTY2MDQ3ODMzNSk7bj1tZDVfZ2cobixtLGwsbyxwW2crNF0sMjAsLTQwNTUzNzg0OCk7bz1tZDVfZ2cobyxuLG0sbCxwW2crOV0sNSw1Njg0NDY0MzgpO2w9bWQ1X2dnKGwsbyxuLG0scFtnKzE0XSw5LC0xMDE5ODAzNjkwKTttPW1kNV9nZyhtLGwsbyxuLHBbZyszXSwxNCwtMTg3MzYzOTYxKTtuPW1kNV9nZyhuLG0sbCxvLHBbZys4XSwyMCwxMTYzNTMxNTAxKTtvPW1kNV9nZyhvLG4sbSxsLHBbZysxM10sNSwtMTQ0NDY4MTQ2Nyk7bD1tZDVfZ2cobCxvLG4sbSxwW2crMl0sOSwtNTE0MDM3ODQpO209bWQ1X2dnKG0sbCxvLG4scFtnKzddLDE0LDE3MzUzMjg0NzMpO249bWQ1X2dnKG4sbSxsLG8scFtnKzEyXSwyMCwtMTkyMTIwNzczNCk7bz1tZDVfaGgobyxuLG0sbCxwW2crNV0sNCwtMzc4NTU4KTtsPW1kNV9oaChsLG8sbixtLHBbZys4XSwxMSwtMjAyMjU3NDQ2Myk7bT1tZDVfaGgobSxsLG8sbixwW2crMTFdLDE2LDE4MzkwMzA1NjIpO249bWQ1X2hoKG4sbSxsLG8scFtnKzE0XSwyMywtMzUzMDk1NTYpO289bWQ1X2hoKG8sbixtLGwscFtnKzFdLDQsLTE1MzA5OTIwNjApO2w9bWQ1X2hoKGwsbyxuLG0scFtnKzRdLDExLDEyNzI4OTMzNTMpO209bWQ1X2hoKG0sbCxvLG4scFtnKzddLDE2LC0xNTU0OTc2MzIpO249bWQ1X2hoKG4sbSxsLG8scFtnKzEwXSwyMywtMTA5NDczMDY0MCk7bz1tZDVfaGgobyxuLG0sbCxwW2crMTNdLDQsNjgxMjc5MTc0KTtsPW1kNV9oaChsLG8sbixtLHBbZyswXSwxMSwtMzU4NTM3MjIyKTttPW1kNV9oaChtLGwsbyxuLHBbZyszXSwxNiwtNzIyODgxOTc5KTtuPW1kNV9oaChuLG0sbCxvLHBbZys2XSwyMyw3NjAyOTE4OSk7bz1tZDVfaGgobyxuLG0sbCxwW2crOV0sNCwtNjQwMzY0NDg3KTtsPW1kNV9oaChsLG8sbixtLHBbZysxMl0sMTEsLTQyMTgxNTgzNSk7bT1tZDVfaGgobSxsLG8sbixwW2crMTVdLDE2LDUzMDc0MjUyMCk7bj1tZDVfaGgobixtLGwsbyxwW2crMl0sMjMsLTk5NTMzODY1MSk7bz1tZDVfaWkobyxuLG0sbCxwW2crMF0sNiwtMTk4NjMwODQ0KTtsPW1kNV9paShsLG8sbixtLHBbZys3XSwxMCwxMTI2MTE2MTQxNSk7bT1tZDVfaWkobSxsLG8sbixwW2crMTRdLDE1LC0xNDE2MzU0OTA1KTtuPW1kNV9paShuLG0sbCxvLHBbZys1XSwyMSwtNTc0MzQwNTUpO289bWQ1X2lpKG8sbixtLGwscFtnKzEyXSw2LDE3MDA0ODU1NzEpO2w9bWQ1X2lpKGwsbyxuLG0scFtnKzNdLDEwLC0xODk0NDQ2NjA2KTttPW1kNV9paShtLGwsbyxuLHBbZysxMF0sMTUsLTEwNTE1MjMpO249bWQ1X2lpKG4sbSxsLG8scFtnKzFdLDIxLC0yMDU0OTIyNzk5KTtvPW1kNV9paShvLG4sbSxsLHBbZys4XSw2LDE4NzMzMTMzNTkpO2w9bWQ1X2lpKGwsbyxuLG0scFtnKzE1XSwxMCwtMzA2MTE3NDQpO209bWQ1X2lpKG0sbCxvLG4scFtnKzZdLDE1LC0xNTYwMTk4MzgwKTtuPW1kNV9paShuLG0sbCxvLHBbZysxM10sMjEsMTMwOTE1MTY0OSk7bz1tZDVfaWkobyxuLG0sbCxwW2crNF0sNiwtMTQ1NTIzMDcwKTtsPW1kNV9paShsLG8sbixtLHBbZysxMV0sMTAsLTExMjAyMTAzNzkpO209bWQ1X2lpKG0sbCxvLG4scFtnKzJdLDE1LDcxODc4NzI1OSk7bj1tZDVfaWkobixtLGwsbyxwW2crOV0sMjEsLTM0MzQ4NTU1MSk7bz1zYWZlX2FkZChvLGopO249c2FmZV9hZGQobixoKTttPXNhZmVfYWRkKG0sZik7bD1zYWZlX2FkZChsLGUpfXJldHVybiBBcnJheShvLG4sbSxsKX1mdW5jdGlvbiBtZDVfY21uKGgsZSxkLGMsZyxmKXtyZXR1cm4gc2FmZV9hZGQoYml0X3JvbChzYWZlX2FkZChzYWZlX2FkZChlLGgpLHNhZmVfYWRkKGMsZikpLGcpLGQpfWZ1bmN0aW9uIG1kNV9mZihnLGYsayxqLGUsaSxoKXtyZXR1cm4gbWQ1X2NtbigoZiZrKXwoKH5mKSZqKSxnLGYsZSxpLGgpfWZ1bmN0aW9uIG1kNV9nZyhnLGYsayxqLGUsaSxoKXtyZXR1cm4gbWQ1X2NtbigoZiZqKXwoayYofmopKSxnLGYsZSxpLGgpfWZ1bmN0aW9uIG1kNV9oaChnLGYsayxqLGUsaSxoKXtyZXR1cm4gbWQ1X2NtbihmXmteaixnLGYsZSxpLGgpfWZ1bmN0aW9uIG1kNV9paShnLGYsayxqLGUsaSxoKXtyZXR1cm4gbWQ1X2NtbihrXihmfCh+aikpLGcsZixlLGksaCl9ZnVuY3Rpb24gY29yZV9obWFjX21kNShjLGYpe3ZhciBlPXN0cjJiaW5sKGMpO2lmKGUubGVuZ3RoPjE2KXtlPWNvcmVfbWQ1KGUsYy5sZW5ndGgqY2hyc3opfXZhciBhPUFycmF5KDE2KSxkPUFycmF5KDE2KTtmb3IodmFyIGI9MDtiPDE2O2IrKyl7YVtiXT1lW2JdXjkwOTUyMjQ4NjtkW2JdPWVbYl1eMTU0OTU1NjgyOH12YXIgZz1jb3JlX21kNShhLmNvbmNhdChzdHIyYmlubChmKSksNTEyK2YubGVuZ3RoKmNocnN6KTtyZXR1cm4gY29yZV9tZDUoZC5jb25jYXQoZyksNTEyKzEyOCl9ZnVuY3Rpb24gc2FmZV9hZGQoYSxkKXt2YXIgYz0oYSY2NTUzNSkrKGQmNjU1MzUpO3ZhciBiPShhPj4xNikrKGQ+PjE2KSsoYz4+MTYpO3JldHVybihiPDwxNil8KGMmNjU1MzUpfWZ1bmN0aW9uIGJpdF9yb2woYSxiKXtyZXR1cm4oYTw8Yil8KGE+Pj4oMzItYikpfWZ1bmN0aW9uIHN0cjJiaW5sKGQpe3ZhciBjPUFycmF5KCk7dmFyIGE9KDE8PGNocnN6KS0xO2Zvcih2YXIgYj0wO2I8ZC5sZW5ndGgqY2hyc3o7Yis9Y2hyc3ope2NbYj4+NV18PShkLmNoYXJDb2RlQXQoYi9jaHJzeikmYSk8PChiJTMyKX1yZXR1cm4gY31mdW5jdGlvbiBiaW5sMnN0cihjKXt2YXIgZD0iIjt2YXIgYT0oMTw8Y2hyc3opLTE7Zm9yKHZhciBiPTA7YjxjLmxlbmd0aCozMjtiKz1jaHJzeil7ZCs9U3RyaW5nLmZyb21DaGFyQ29kZSgoY1tiPj41XT4+PihiJTMyKSkmYSl9cmV0dXJuIGR9ZnVuY3Rpb24gYmlubDJoZXgoYyl7dmFyIGI9aGV4Y2FzZT8iMDEyMzQ1Njc4OUFCQ0RFRiI6IjAxMjM0NTY3ODlhYmNkZWYiO3ZhciBkPSIiO2Zvcih2YXIgYT0wO2E8Yy5sZW5ndGgqNDthKyspe2QrPWIuY2hhckF0KChjW2E+PjJdPj4oKGElNCkqOCs0KSkmMTUpK2IuY2hhckF0KChjW2E+PjJdPj4oKGElNCkqOCkpJjE1KX1yZXR1cm4gZH1mdW5jdGlvbiBiaW5sMmI2NChkKXt2YXIgYz0iQUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkrLyI7dmFyIGY9IiI7Zm9yKHZhciBiPTA7YjxkLmxlbmd0aCo0O2IrPTMpe3ZhciBlPSgoKGRbYj4+Ml0+PjgqKGIlNCkpJjI1NSk8PDE2KXwoKChkW2IrMT4+Ml0+PjgqKChiKzEpJTQpKSYyNTUpPDw4KXwoKGRbYisyPj4yXT4+OCooKGIrMiklNCkpJjI1NSk7Zm9yKHZhciBhPTA7YTw0O2ErKyl7aWYoYio4K2EqNj5kLmxlbmd0aCozMil7Zis9YjY0cGFkfWVsc2V7Zis9Yy5jaGFyQXQoKGU+PjYqKDMtYSkpJjYzKX19fXJldHVybiBmfTt3aW5kb3cuZiA9IGhleF9tZDUobXdxcXBweik='
    eval(window.atob(window['b'])["replace"]("mwqqppz", '\x27' + mw + '\x27'));
    return ''
}
oo0O0(Date['\x70\x61\x72\x73\x65'](new Date()) + (16798545 + -72936737 + 156138192).toString())
console.log(window.f)