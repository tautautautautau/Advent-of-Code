var fs = require("fs");
var iA = fs.readFileSync("input/iA19.txt").toString().split("\r\n\r\n");

let rules = iA[0].split("\r\n");
let strings = iA[1].split("\r\n");

rules = rules.map(row => row.split(": "));
for (let i = 0; i < rules.length; i++) {
    rules[i][1] = rules[i][1].split(" | ");
}
for (let i = 0; i < rules.length; i++) {
    for (let j = 0; j < rules[i][1].length; j++) {
        rules[i][1][j] = rules[i][1][j].split(" ");
    }
}
rules.sort((a, b) => a[0] - b[0]);

let ruleMap = new Map();
rules.forEach(rule => ruleMap.set(rule[0], rule[1]));

console.log(ruleMap);