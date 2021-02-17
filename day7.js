let fs = require("fs");
let iA = fs.readFileSync("input/iA7.txt").toString().split("\n");

let bags = new Map();

iA.forEach(rule => {
    let bag = rule.split(" ")[0] + " " + rule.split(" ")[1];
    let rules = rule.match(/[1-9] [a-z]+ [a-z]+/g);
    if (rules) {
        for (let i = 0; i < rules.length; i++) {
            let e = rules[i], t = parseInt(e.substr(0, 1)), b = e.substr(2), h = [];
            for (let j = 0; j < t; j++) h.push(b);
            rules[i] = h;
        }
        rules = rules.flat();
    }
    if (!bags.get(bag)) bags.set(bag, rules);
});

let x = [], totalBags = [];
bags.forEach((value, key) => {if (value) if (value.includes("shiny gold")) x.push(key)});
for (let i = 0; i < x.length; i++) bags.forEach((value, key) => {if (value) if (value.includes(x[i])) x.push(key)});
getBags("shiny gold");

// PART 1
console.log((x.filter((a, b) => x.indexOf(a) === b)).length);
// PART 2
console.log(totalBags.length);

function getBags(bag) {
    let value = bags.get(bag);
    if (value) {
        totalBags.push(...value);
        value.forEach(e => getBags(e));
    } else return null;
}