def dec_to_snafu(n: int) -> str:
	ret = ""
	while n:
		remainder = n % 5
		ret += table.get(remainder)
		n //= 5
		n += remainder // 3
	return ret[::-1]


def snafu_to_dec(snafu: str) -> int:
	ret = 0
	for idx, char in enumerate(snafu[::-1]):
		ret += rev_table.get(char) * (5 ** idx)
	return ret


table = {
	4: "-",
	3: "=",
	2: "2",
	1: "1",
	0: "0"
}


rev_table = {
	"2": 2,
	"1": 1,
	"0": 0,
	"-": -1,
	"=": -2
}


data = [line.strip() for line in open("day25.txt", "r")]

total = 0
for line in data:
	dec = snafu_to_dec(line)
	total += dec

print(dec_to_snafu(total))
