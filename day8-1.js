let fs = require("fs");
let iA = fs.readFileSync("input/iA8.txt").toString().split("\n");
let insA = [], acc = 0, lines = [], i = 0;
iA.forEach(ins => insA.push(ins.split(" ")));
while (!lines.includes(i) && i < insA.length) {
    lines.push(i);
    (insA[i][0] == "jmp") ? i += +insA[i][1] : (insA[i][0] == "nop") ? i++ : (acc += +insA[i][1], i++);
}
console.log(acc);