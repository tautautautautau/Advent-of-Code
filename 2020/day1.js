var fs = require("fs");
var iA = fs.readFileSync("input/iA1.txt").toString().split("\n");

part1([...iA]);
part2([...iA]);

// PART 1
function part1(iA) {
  for (let i = 0; i < iA.length; i++) {
    for (let j = i + 1; j < iA.length; j++) {
      let a = parseInt(iA[i]),b = parseInt(iA[j]);
      if (a + b == 2020) console.log(a * b);
    }
  }
}

// PART 2
function part2(iA) {
  for (let i = 0; i < iA.length; i++) {
    for (let j = i + 1; j < iA.length; j++) {
      for (let k = j + 1; k < iA.length; k++) {
        let a = parseInt(iA[i]),b = parseInt(iA[j]),c = parseInt(iA[k]);
        if (a + b + c == 2020) console.log(a * b * c);
      }
    }
  }
}