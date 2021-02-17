let fs = require("fs");
let iA = fs.readFileSync("input/iA6.txt").toString().split("\n\n");

let groupYesAnswers = [];

iA.forEach(group => {
    let yesAnswers = new Map();
    group.replace(/\n/g, "").split("").forEach(answer => {
        (yesAnswers.get(answer)) ? yesAnswers.set(answer, yesAnswers.get(answer) + 1) : yesAnswers.set(answer, 1);
    });
    groupYesAnswers.push([group.split("\n").length, yesAnswers]);
});

let total = [0, 0];
groupYesAnswers.forEach(group => {
    total[0] += group[1].size;
    group[1].forEach((value) => {if (value == group[0]) total[1]++});
});

// PART 1
console.log(total[0]);
// PART 2
console.log(total[1]);