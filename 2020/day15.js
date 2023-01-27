let iA = "2,0,1,7,4,14,18".split(',').map(x => +x);

// PART 1
console.log(run(2020));
// PART 2
console.log(run(30000000));

function run(nth) {
    let saidNumbers = new Map();
    for (let i = 0; i < iA.length; i++)  saidNumbers.set(iA[i], i+1);
    let last = iA[iA.length - 1];
    for (let i = iA.length + 1; i <= nth; i++) {
        let next;
        (saidNumbers.has(last)) ? next = i - 1 - saidNumbers.get(last) : next = 0;
        saidNumbers.set(last, i-1);
        last = next;
    }
    return last;
}