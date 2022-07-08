
var Location = function Location() {  //构造函数
    throw new TypeError("Illegal constructor");
}; catvm.safefunction(Location);


Object.defineProperties(Location.prototype, {
    [Symbol.toStringTag]: {
        value: "Location",
        configurable: true
    }
})

/////////////////////////////




location = {};
location.__proto__ = Location.prototype;

location.hash = "",
location.host = "www.douyin.com",
location.hostname = "www.douyin.com",
location.href = "https://www.douyin.com/",
location.origin = "https://www.douyin.com",
location.pathname = "/",
location.port = "",
location.protocol = "https"
location.search = "?source=switch_tab&type=user"



for (let prototype_ in Location.prototype) {
    location[prototype_] = Location.prototype[prototype_];

    Location.prototype.__defineGetter__(prototype_, function () {
        debugger;
        throw new TypeError("Illegal constructor");

    });


}

/////////////////////////////


location = catvm.proxy(location);