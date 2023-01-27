test_data = [
	"root: pppw + sjmn",
	"dbpl: 5",
	"cczh: sllz + lgvd",
	"zczc: 2",
	"ptdq: humn - dvpt",
	"dvpt: 3",
	"lfqf: 4",
	"humn: 5",
	"ljgn: 2",
	"sjmn: drzm * dbpl",
	"sllz: 4",
	"pppw: cczh / lfqf",
	"lgvd: ljgn * ptdq",
	"drzm: hmdt - zczc",
	"hmdt: 32"
]


class Monkey:
	def __init__(self, name, job):
		self.name = name
		self.job = job


monkeys = list()

for line in test_data:
	monkeys.append(Monkey(*line.split(": ")))

for monkey in monkeys:
	print(monkey.name)
	print("	", monkey.job)
