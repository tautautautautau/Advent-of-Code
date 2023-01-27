var fs = require("fs");
var iA = fs.readFileSync("input/iA3.txt").toString().split("\n");
iA.forEach(row => row.split(""));
let x = [0, 0, 0, 0, 0], y = 0, width = iA[0].length, trees = [0, 0, 0, 0, 0];
while (y < iA.length - 1) {
    for (let i = 0; i < x.length - 1; i++) if (iA[y][x[i]] == "#") trees[i]++;
    if (y % 2 == 0) {if (iA[y][x[4]] == "#") trees[4]++; x[4]++;}
    y++;x[0]++;x[1] += 3;x[2] += 5;x[3] += 7;
	for (let i = 0; i < x.length; i++) if (x[i] >= width) x[i] -= width;
}
// PART 1
console.log(trees[1]);
// PART 2
console.log(trees.reduce((a, b) => a * b));