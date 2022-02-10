//框架代理功能
lhvm.proxy = function (o) {
    if (lhvm.memory.config.proxy == false) {
        return o
    }
    return new Proxy(o, {
        set(target, property, receiver) {
            console.log("set", target, property, target[property])
            return Reflect.set(...arguments);
        },
        get(target, property, receiver) {
            console.log("get", target, property, target[property])
            return target[property]
        }
    })
}