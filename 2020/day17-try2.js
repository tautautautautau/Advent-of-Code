let fs = require("fs");
let iA = fs.readFileSync("input/iA17.txt").toString().split("\n");
iA = iA.map(row => row.split("")).map((x,i) => iA.map(x => x[i])).map(sub => {return sub.map(entry => {return [entry];});});

let temp = [];

for (let cycle = 0; cycle < 6; cycle++) {
    let updates = [];
    for (let x = 0; x < iA.length; x++) {
        for (let y = 0; y < iA[0].length; y++) {
            for (let z = 0; z < iA[0][0].length; z++) {
                let val = iA[x][y][z];
                let newVal = update(x, y, z);
                if (newVal != val) updates.push([x, y, z, newVal]);
            }
        }
    }
    updates.forEach(updateArr => iA[updateArr[0]][updateArr[1]][updateArr[2]] = updateArr[3]);
    console.log(temp);
}

let active = 0;
for (let x = 0; x < iA.length; x++) {
    for (let y = 0; y < iA[x].length; y++) {
        for (let z = 0; z < iA[x][y].length; z++) {
            if (iA[x][y][z] == "#") active++;
        }
    }
}
console.log(active);

function update(a, b, c) {
    let activeNeighbors = 0;
    a = +a;
    b = +b;
    c = +c;
    for (let x = -1; x < 2; x++) {
        for (let y = -1; y < 2; y++) {
            for (let z = -1; z < 2; z++) {
                if (iA[a+x] != undefined) {
                    if (iA[a+x][b+y] != undefined) {
                        if (iA[a+x][b+y][c+z] != undefined) {
                            if (iA[a+x][b+y][c+z] == "#") activeNeighbors++;
                        }
                    }
                } else {
                    temp[a+x] = [];
                    temp[a+x][b+y] = [];
                    temp[a+x][b+y][c+z] = ".";
                }
            }
        }
    }
    let returnValue;
    if (iA[a][b][c] == "#") {
        (activeNeighbors == 2 || activeNeighbors == 3) ? returnValue = "#" : returnValue = ".";
    } else if (iA[a][b][c] == ".") {
        (activeNeighbors == 3) ? returnValue = "#" : returnValue = ".";
    } else return error("Value does not match (.) or (#)");
    return returnValue;
}