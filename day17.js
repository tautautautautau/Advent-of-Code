const { error } = require("console");
let fs = require("fs");
let iA = fs.readFileSync("2020/input/iA17.txt").toString().split("\n");
iA = iA.map(row => row.split(""));
iA = iA[0].map((x,i) => iA.map(x => x[i]));

let space = new Map(), tempSpace = new Map();
for (let i = 0; i < iA.length; i++)
    for (let j = 0; j < iA[0].length; j++)
        space.set([j, i, 0].toString(), iA[j][i]);

for (let cycle = 0; cycle < 6; cycle++) {
    space.forEach((value, key) => update(key, value));
    tempSpace.forEach((value, key) => space.set(key, value));
    tempSpace.clear();
}

let active = 0;
space.forEach(value => {if (value == "#") active++;});
console.log(active);

function update(xyz, value) {
    let activeNeighbors = 0;
    for (let x = -1; x <= 1; x++) {
        for (let y = -1; y <= 1; y++) {
            for (let z = -1; z <= 1; z++) {
                if (x != 0 || y != 0 || z != 0) {
                    let abc = xyz.split(",");
                    let a = parseInt(abc[0]) + x;
                    let b = parseInt(abc[1]) + y;
                    let c = parseInt(abc[2]) + z;
                    let point = [a, b, c].toString();
                    if (space.has(point)) {
                        if (space.get(point) == "#") activeNeighbors++;
                    } else tempSpace.set(point, ".");
                }
            }
        }
    }
    let returnValue;
    if (value == "#") {
        (activeNeighbors == 2 || activeNeighbors == 3) ? returnValue = "#" : returnValue = ".";
    } else if (value == ".") {
        (activeNeighbors == 3) ? returnValue = "#" : returnValue = ".";
    } else return error("Value does not match(.) or (#)");
    tempSpace.set(xyz, returnValue);
}