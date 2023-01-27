let fs = require("fs");
let iA = fs.readFileSync("input/iA5.txt").toString().split("\n");

let IDs = [];

iA.forEach(e => {
    IDs.push((getPos(e.substr(0, 7).split(""), 0, [0, 127]) * 8)
     + getPos(e.substr(7).split(""), 0, [0, 7]));
});
IDs.sort((a, b) => a - b);

// PART 1
console.log(IDs[IDs.length - 1]);

// PART 2
for (let i = IDs[1]; i < IDs[IDs.length - 1]; i++) {
    if (!IDs.includes(i) && IDs.includes(i - 1) && IDs.includes(i + 1))
        console.log(i);
}

function getPos(a, i, range) {
    if (i == a.length - 1) {
        if (a[i] == "F" || a[i] == "L") return range[0];
        if (a[i] == "B" || a[i] == "R") return range[1];
    }
    if (a[i] == "F" || a[i] == "L") range[1] = Math.floor((range[1] + range[0]) / 2);
    if (a[i] == "B" || a[i] == "R") range[0] = Math.ceil((range[1] + range[0]) / 2);
    return getPos(a, ++i, range);
}