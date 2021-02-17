let fs = require("fs");
let iA = fs.readFileSync("input/iA10.txt").toString().split("\n");
iA.push(0);
iA.push(Math.max(...iA) + 3);
let sortedArr = iA.sort((a, b) => a - b);

// PART 1
let p1Output = part1(sortedArr);
console.log(countOccurrences(p1Output, 1) * countOccurrences(p1Output, 3));
// PART 2
let p2Output = part2(sortedArr);
console.log(p2Output.pop());

function part1(array) {
    let diffs = [];
    for (let i = 0; i < array.length; i++) diffs.push(array[i + 1] - array[i]);
    return diffs;
}

function part2(array) {
    let out = new Array(array.length).fill(0);
    out[0] = 1;
    for (let i = 1; i < array.length; i++) {
        for (let j = 0; j < i; j++) {
            if (array[i] - array[j] <= 3) out[i] += out[j];
        }
    }
    return out;
}

function countOccurrences(arr, val) {
    return arr.reduce((a, v) => (v == val ? a + 1 : a), 0);
}