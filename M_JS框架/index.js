var fs = require("fs")
var lhvm = require("./LhVm/lhvm.node")
const {VM, VMScript} = require("vm2")
const lhvmcode = lhvm.GetCode();
const codefile = `${__dirname}/code.js`
const vm = new VM()
const script = new VMScript(lhvmcode + fs.readFileSync(codefile), "VM2")
debugger
vm.run(script)
debugger


