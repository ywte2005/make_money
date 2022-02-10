var people = {
    "name": "lyb"
};
var count = 18;
Object.defineProperty(people, "age", {
    get: function () {
        console.log("获取了！！")
        return count
    },
    set: function (val) {
        console.log("设置了")
        return count = val + 1
    }
})
console.log(people.age)
people.age=20
console.log(people.age)

