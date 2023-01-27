data = open("input/day11.txt").read()
monkeys_data = data.split("\n\n")


class MONKEY:
    def __init__(self, number, items, operation, test, if_true, if_false):
        self.number = int(number)
        self.items = list(items)
        self.operation = operation
        self.test = int(test)
        self.if_true = int(if_true)
        self.if_false = int(if_false)
        self.items_handled = 0

    def handle(self):
        while self.items:
            item = int(self.items.pop(0))
            operation, amount = self.operation.split()
            operation = operation.strip()
            if amount == "old":
                amount = item
            else:
                amount = int(amount)
            new = 0
            match operation:
                case "*":
                    new = item * amount
                case "+":
                    new = item + amount
            #new = round(new // 3)
            new %= mod_factor
            if new % self.test == 0:
                monkeys[self.if_true].add_item(new)
            else:
                monkeys[self.if_false].add_item(new)
            self.items_handled += 1

    def add_item(self, item):
        self.items.append(item)


def print_monkeys():
    for monkey in monkeys:
        print(f"Monkey {monkey.number}: {monkey.items}")
    print()


monkeys = []
for monkey in monkeys_data:
    monkey_lines = monkey.splitlines()
    _, num = monkey_lines[0][:-1].split()
    num = int(num)
    _, start_items = monkey_lines[1].split(":")
    start_items = start_items.split(", ")
    start_items = list(map(int, start_items))
    _, operation = monkey_lines[2].split("old ")
    _, test = monkey_lines[3].split("by ")
    _, if_true = monkey_lines[4].split("monkey ")
    if_true = int(if_true)
    _, if_false = monkey_lines[5].split("monkey ")
    if_false = int(if_false)
    monkeys.append(MONKEY(num, start_items,
                   operation.strip(), test.strip(),
                   if_true, if_false))

mod_factor = 1
for monkey in monkeys:
    mod_factor *= monkey.test

for r in range(10000):
    for monkey in monkeys:
        monkey.handle()

handling_counts = list()
for monkey in monkeys:
    handling_counts.append(monkey.items_handled)
print(handling_counts)
handling_counts.sort(reverse=True)
print(handling_counts[0] * handling_counts[1])
