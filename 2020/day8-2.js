let fs = require("fs");
let iA = fs.readFileSync("input/iA8.txt").toString().split("\n");

let instructions = [];
iA.forEach(instruction => instructions.push(instruction.split(" ")));

for (let i = 0; i < instructions.length; i++) {
    if (instructions[i][0] != "acc") {
        swap(i);
        let output = run(instructions);
        swap(i);
        if (output[0]) console.log(output[1]);
    }
}

function run(array) {
    let acc = 0, ranLines = [], i = 0;
    while (!ranLines.includes(i) && i < array.length) {
        ranLines.push(i);
        if (array[i][0] == "nop") {
            i++;
        } else if (array[i][0] == "jmp") {
            i += parseInt(array[i][1]);
        } else if (array[i][0] == "acc") {
            acc += parseInt(array[i][1]);
            i++;
        }
    }
    return [i == array.length, acc];
}

function swap(i) {
    if (instructions[i][0] == "jmp") {
        instructions[i][0] = "nop";
    } else if (instructions[i][0] == "nop") {
        instructions[i][0] = "jmp";
    }
}

// Thanks https://github.com/zecookiez/AdventOfCode2020/blob/main/day08_handheld_halting.py