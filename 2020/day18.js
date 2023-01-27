var fs = require("fs");
var iA = fs.readFileSync("input/iA18.txt").toString().split("\n");
var stringMathNoOrder = require('./string-math-noorder');
var stringMathAddSub = require('./string-math-addsubfirst');
// PART 1
let total = 0;
iA.forEach(e => total += stringMathNoOrder(e));
console.log(total);
// PART 2
total = 0;
iA.forEach(e => total += stringMathAddSub(e));
console.log(total);