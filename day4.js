var fs = require("fs");
var iA = fs.readFileSync("input/iA4.txt").toString().split("\n");

let i = 0, valid = 0, valid2 = 0, passports = [];
let reqs = ["byr","iyr","eyr","hgt","hcl","ecl","pid"];
let eyeColors = ["amb","blu","brn","gry","grn","hzl","oth"];

iA.forEach(row => {
	if (!passports[i]) passports[i] = [];
	(row != "") ? passports[i] = passports[i].concat(row.split(" ")) : i++;
});

passports.forEach(passport => {
	if (reqs.every(req => (passport.join(" ")).includes(req))) {
		valid++;
		let validFields = 0;
		passport.forEach((field) => {
			value = field.substr(4);
			switch (field.substr(0, 3)) {
				case "byr":
					if (parseInt(value) >= 1920 && parseInt(value) <= 2002) validFields++;
					break;
				case "iyr":
					if (parseInt(value) >= 2010 && parseInt(value) <= 2020) validFields++;
					break;
				case "eyr":
					if (parseInt(value) >= 2020 && parseInt(value) <= 2030) validFields++;
					break;
				case "hgt":
					if (value.endsWith("in")) {
						if (parseInt(value) >= 59 && parseInt(value) <= 76) validFields++;
					} else if (value.endsWith("cm")) {
						if (parseInt(value) >= 150 && parseInt(value) <= 193) validFields++;
					}
					break;
				case "hcl":
					if (value.match("^#([a-f0-9]{6})$")) validFields++;
					break;
				case "ecl":
					if (eyeColors.some(color => value.includes(color))) validFields++;
					break;
				case "pid":
					if (value.match("^([0-9]{9})$")) validFields++;
					break;
			}
		});
		if (validFields == 7) valid2++;
	};
});

// PART 1
console.log(valid);
// PART 2
console.log(valid2);