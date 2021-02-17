let fs = require("fs");
let iA = fs.readFileSync("input/iA12.txt").toString().split("\n");
iA = iA.map(row => [row.substr(0,1), parseInt(row.substr(1))]);
let directions = ["N", "E", "S", "W"];

let position = [0, 0];
let facing = "E";

let waypoint = [10, 1];

// PART 1
// iA.forEach(row => {
//     if (row[0] == "R" || row[0] == "L") turn(row[0], row[1]);
//     else move(row[0], row[1]);
// });

// PART 2
iA.forEach(row => {
    if (row[0] == "F") moveTowardsWaypoint(row[1]);
    if (row[0] == "R" || row[0] == "L") rotate(row[0], row[1]);
    else moveWaypoint(row[0], row[1]);
    //console.log("Ship ->", position, "Waypoint ->", waypoint);
});

console.log(Math.abs(position[0]) + Math.abs(position[1]));

function move(dir, amount) {
    if (dir == "F") {
        move(facing, amount);
    }
    if (dir == "N") {
        position[1] += amount;
    }
    if (dir == "S") {
        position[1] -= amount;
    }
    if (dir == "W") {
        position[0] -= amount;
    }
    if (dir == "E") {
        position[0] += amount;
    }
}

function turn(dir, amount) {
    let newFacing;
    let facingIndex = directions.indexOf(facing);
    let times = parseInt(amount / 90);
    for (let i = 0; i < times; i++) {
        if (dir == "L") facingIndex--;
        if (dir == "R") facingIndex++;
        if (facingIndex < 0) facingIndex = directions.length - 1;
        if (facingIndex > directions.length - 1) facingIndex = 0;
        newFacing = directions[facingIndex];
    }
    facing = newFacing;
}

function moveTowardsWaypoint(times) {
    position[0] += (waypoint[0] * times);
    position[1] += (waypoint[1] * times);
}

function rotate(dir, amount) {
    for (let i = 0; i < parseInt(amount / 90); i++) {
        if (dir == "R") waypoint = [waypoint[1], -1 * waypoint[0]]; //90 clockwise = (x,y) -> (y,-x)
        if (dir == "L") waypoint = [-1 * waypoint[1], waypoint[0]]; //90 counterclockwise = (x,y) -> (-y,x)
    }
}

function moveWaypoint(dir, amount) {
    if (dir == "N") waypoint[1] += amount;
    else if (dir == "S") waypoint[1] -= amount;
    else if (dir == "E") waypoint[0] += amount;
    else if (dir == "W") waypoint[0] -= amount;
}