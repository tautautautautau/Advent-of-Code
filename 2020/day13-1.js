var fs = require("fs");
var iA = fs.readFileSync("input/iA13.txt").toString().split("\n");
const { getRawInput, runTests, modulo, bigIntChineseRemainder } = require("./lib");

let timeNow = iA[0];
let busses = iA[1].split(",");

let times = [];

busses.forEach(bus => {
    if (bus != "x") {
        let time = 0;
        while (time < timeNow) {
            time += parseInt(bus);
        }
        times.push([(time - timeNow), parseInt(bus)]);
    }
});

let least = 0;
for (let i = 1; i < times.length; i++) {
    if (times[i][0] < times[least][0]) least = i;
}

console.log(times[least][0] * times[least][1]);

let busIndexes = [];
for (let i = 0; i < busses.length; i++) {
    if (busses[i] != "x") {
        busIndexes.push([BigInt(modulo(-i, busses[i])), BigInt(busses[i])]);
    }
}

console.log(bigIntChineseRemainder(...busIndexes));