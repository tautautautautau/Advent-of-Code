var fs = require("fs");
var iA = fs.readFileSync("input/iA16.txt").toString().split("\n\n");

let notes = iA[0].split("\n").map(line => line.match(/\d+-\d+/g).map(section => section.split("-")));
let myTicket = iA[1].split("\n")[1].split(",");
let nearbyTickets = iA[2].split("\n").map(row => row.split(","));
nearbyTickets.shift();

let invalidValues = [];
let validTickets = [];
nearbyTickets.forEach(ticket => {
    let ticketsInvalids = [];
    ticket.forEach(value => {
        let valid = false;
        let v = parseInt(value);
        for (let i = 0; i < notes.length; i++) {
            let min1 = parseInt(notes[i][0][0]), max1 = parseInt(notes[i][0][1]),
                min2 = parseInt(notes[i][1][0]), max2 = parseInt(notes[i][1][1]);
            if ((v >= min1 && v <= max1) || (v >= min2 && v <= max2)) valid = true;
        }
        if (!valid) ticketsInvalids.push(v);
    });
    if (ticketsInvalids.length == 0) validTickets.push(ticket);
    invalidValues.push(...ticketsInvalids);
});

// PART 1
console.log(invalidValues.reduce((a, b) => a + b));

let fields = [];

for (let i = 0; i < 20; i++) {
    for (let j = 0; j < validTickets.length; j++) {
        (fields[i]) ? fields[i].push(validTickets[j][i]) : fields[i] = [validTickets[j][i]];
    }
}

//    TICKET         MATCHES NOTE
//validFields[0] = [true, false, true];

let validFields = new Array(20).fill([]);

for (let i = 0; i < fields.length; i++) {
    let v = [];
    for (let j = 0; j < notes.length; j++) {
        let min1 = parseInt(notes[j][0][0]), max1 = parseInt(notes[j][0][1]),
            min2 = parseInt(notes[j][1][0]), max2 = parseInt(notes[j][1][1]);
        for (let k = 0; k < fields[i].length; k++) {
            let x = fields[i][k];
            if ((x >= min1 && x <= max1) || (x >= min2 && x <= max2)) {
                (v[k]) ? v[k].push(true) : v[k] = [true];
            } else (v[k]) ? v[k].push(false) : v[k] = [false];
        }
    }
    (v[i].every(x => x == true)) ? validFields[i].push(true) : validFields[i].push(false);
}

console.log(validFields);