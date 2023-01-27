let fs = require("fs");
let iA = fs.readFileSync("input/iA14.txt").toString().split("\n");

// PART 1
let memory = new Map();
let mask = "";
for (let i = 0; i < iA.length; i++) {
    let splitted = iA[i].split(" = ");
    let ins = splitted[0];
    let val = splitted[1];
    if (ins == "mask") mask = val;
    if (ins != "mask") {
        val = createBinaryString(val);
        let maskArr = mask.split("");
        let valArr = val.split("");
        for (let a = 0; a < mask.length; a++) {
            if (mask[a] != "X") valArr[a] = maskArr[a];
        }
        val = parseInt(valArr.join(""), 2);
        memory.set(ins.match(/\[(\d+)\]/)[1], val);
    }
}
let total = 0;
memory.forEach((value, key) => total += value);
console.log(total);

// PART 2
memory = new Map();
mask = "";
for (let i = 0; i < iA.length; i++) {
    let splitted = iA[i].split(" = ");
    let ins = splitted[0];
    let val = splitted[1];
    if (ins == "mask") mask = val;
    if (ins != "mask") {
        let memAddress = ins.match(/\[(\d+)\]/)[1];
        let memAddressBin = createBinaryString(memAddress);
        let maskArr = mask.split("");
        let memAddressBinArr = mask.split("");
        for (let a = 0; a < mask.length; a++) if (maskArr[a] != "0") memAddressBinArr[a] = maskArr[a];
        let xs = 0;
        for (let b = 0; b < memAddressBinArr.length; b++) if (memAddressBinArr[b] == "X") xs++;
        xs = Math.pow(2, xs);
        let addresses = new Array(xs).fill(memAddressBin);
        let amount = xs / 2;
        let digit = "0";
        for (let i = 0; i < memAddressBinArr.length; i++) {
            const bit = memAddressBinArr[i];
            let times = 0;
            if (bit != "X") addresses.forEach(address => address += bit);
            else {
                for (let j = 0; j < addresses.length; j++) {
                    addresses[j] += digit;
                    times++;
                    if (times > amount) {
                        times = 0;
                        (digit = "0") ? digit = "1" : digit = "0";
                    }
                }
                amount /= 2;
            }
        }
        console.log(addresses);
        addresses.forEach(address => {
            address = parseInt(address, 2);
            memory.set(address, val);
        });
    }
}
total = 0;
memory.forEach((value, key) => total += value);
console.log(total);

function createBinaryString (nMask) {
    // nMask must be between -2147483648 and 2147483647
    for (var nFlag = 0, nShifted = nMask, sMask = ""; nFlag < 32;
        nFlag++, sMask += String(nShifted >>> 31), nShifted <<= 1);
    return "0000" + sMask;
}