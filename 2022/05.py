import re

data = open("input/day5.txt").read()
crates, instructions = data.split("\n\n")
crates = crates.splitlines()
crates_per_line = len(crates[0]) // 4 + 1

stacks_a = [[] for _ in range(crates_per_line)]
stacks_b = [[] for _ in range(crates_per_line)]
for line in crates:
    for i in range(crates_per_line):
        element = line[i * 4 + 1: i * 4 + 3 - 1]
        if element in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            stacks_a[i].insert(0, element)
            stacks_b[i].insert(0, element)

for instruction in instructions.splitlines():
    amount, from_stack, to_stack = map(int, re.findall(r"\d+", instruction))
    crane = []
    for _ in range(amount):
        stacks_a[to_stack - 1].append(stacks_a[from_stack - 1].pop())
        crane.insert(0, stacks_b[from_stack - 1].pop())
    stacks_b[to_stack - 1].extend(crane)

answer_a = ""
answer_b = ""
for stack_a, stack_b in zip(stacks_a, stacks_b):
    answer_a += stack_a[-1]
    answer_b += stack_b[-1]
print(answer_a, answer_b)
