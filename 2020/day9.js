let fs = require("fs");
let iA = fs.readFileSync("input/iA9.txt").toString().split("\n").map(x => x = parseInt(x));

let invalid = 0;

for (let i = 25; i < iA.length; i++) {
    const number = iA[i];
    const prev25 = iA.slice(i - 25, i);
    let valid = [];
    for (let x = 0; x < prev25.length - 1; x++) {
        for (let y = x + 1; y < prev25.length; y++) {
            valid.push(prev25[x] + prev25[y] == number);
        }
    }
    if (!valid.includes(true)) invalid = iA[i], i = iA.length;
}

// PART 1
console.log(invalid);

// PART 2
for (let i = 0; i < iA.length; i++) {
    let k = i + 1;
    let contiguousRange = iA.slice(i, k + 1);
    let sum = contiguousRange.reduce((a, b) => a + b);
    while (k <= iA.length && sum < invalid) {
        contiguousRange = iA.slice(i, ++k);
        sum = contiguousRange.reduce((a, b) => a + b);
    }
    if (sum == invalid) i = iA.length, console.log(Math.max(...contiguousRange) + Math.min(...contiguousRange));
}