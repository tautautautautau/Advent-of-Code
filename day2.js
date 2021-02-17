var fs = require("fs");
var iA = fs.readFileSync("input/iA2.txt").toString().split("\n");

let totalValid = [0, 0];
for (let i = 0; i < iA.length; i++) {
    const r = iA[i];
    let rules = r.split(":")[0];
    let pass = (r.split(":")[1]).trim();
    let min = parseInt((rules.split(" ")[0]).split("-")[0]);
    let max = parseInt((rules.split(" ")[0]).split("-")[1]);
    let letter = (rules.split(" ")[1]);
    let passLettersArray = pass.split("");
    let amount = 0;
    passLettersArray.forEach(l => {
        if (l==letter) amount++;
    });
    if ((amount>=min)&&(amount<=max)) totalValid[0]++;
    if (
        (passLettersArray[min - 1] == letter) ^
        (passLettersArray[max - 1] == letter)
      )
        totalValid[1]++;
}

// PART 1
console.log(totalValid[0]);
// PART 2
console.log(totalValid[1]);