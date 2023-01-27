var fs = require("fs");
const { modulo, bigIntChineseRemainder } = require('./lib');

const rawInput = fs.readFileSync("input/iA13.txt").toString()
const input = parseInput(rawInput);

console.log(run(input));

function run(buses) {
	const N = buses.map(([bus, offset]) => BigInt(bus));
    const A = buses.map(([bus, offset]) => BigInt(modulo(-offset, bus)));
    console.log(buses, "\nN->", N, "\nA->", A);
	return Number(bigIntChineseRemainder(A, N));
}

function parseInput(str) {
	const [line1, line2] = str.split('\n');
	const buses = line2.split(',')
		.map((x,i) => [x,i])
		.filter(([x,i]) => x !== 'x')
		.map(([x,i]) => [+x,i]);
	return buses;
}
