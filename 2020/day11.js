let fs = require("fs");
let iA = fs.readFileSync("input/iA11.txt").toString().split("\n");
for (let i = 0; i < iA.length; i++) iA[i] = iA[i].split('');

let stop = false;
while (!stop) {
    let changed = 0;
    let iB = JSON.parse(JSON.stringify(iA));
    iA = JSON.parse(JSON.stringify(part2(iA)));
    for (let i = 0; i < iA.length; i++)
        for (let j = 0; j < iA[0].length; j++)
            if (iA[i][j] != iB[i][j]) changed++;
    if (changed == 0) stop = true;
}
console.log(countOccurrences(JSON.parse(JSON.stringify(iA)).flat(), "#"));

function part1(arr) {
    let array = JSON.parse(JSON.stringify(arr));
    for (let i = 0; i < arr.length; i++)
        for (let j = 0; j < arr[0].length; j++)
            array[i][j] = checkAdjacent(i, j, arr);
    return array;
}

function part2(arr) {
    let array = JSON.parse(JSON.stringify(arr));
    let dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]];
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[0].length; j++) {
            let occupied = 0;
            dirs.forEach(dir => {if (firstOccupied(i, j, dir, arr)) occupied++;});
            if (arr[i][j] == "#" && occupied >= 5) array[i][j] = "L";
            if (arr[i][j] == "L" && occupied == 0) array[i][j] = "#";
        }
    }
    return array;
}

function countOccurrences(arr, val) {
    return arr.reduce((a, v) => (v == val ? a + 1 : a), 0);
}

function checkAdjacent(i, j, arr) {
    let dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]];
    let occupied = 0;
    dirs.forEach(dir => {
        if (typeof arr[i+dir[0]] != 'undefined')
            if (typeof arr[i+dir[0]][j+dir[1]] != 'undefined')
                if (arr[i+dir[0]][j+dir[1]] == "#") occupied++;});
    if (arr[i][j] == "L" && occupied == 0) return "#";
    if (arr[i][j] == "#" && occupied >= 4) return "L";
    return arr[i][j];
}

function firstOccupied(i, j, dir, arr) {
    let loop = 1;
    while (true) {
        let x = dir[0]*loop, y = dir[1]*loop;
        if (typeof arr[i+x] != 'undefined')
            if (typeof arr[i+x][j+y] != 'undefined') {
                if (arr[i+x][j+y] != ".") return (arr[i+x][j+y] == "#");
                loop++;
            }
            else return false;
        else return false;
    }
}