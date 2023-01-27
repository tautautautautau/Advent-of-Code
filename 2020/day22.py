with open("input/iA22.txt") as f:
    lines = f.read()

p1, p2 = lines.split("\n\n")
p1 = p1.split("\n")[1:]
p2 = p2.split("\n")[1:]
p1 = [int(i) for i in p1]
p2 = [int(i) for i in p2]

def part1(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        p1Card = p1.pop(0)
        p2Card = p2.pop(0)
        if p1Card > p2Card:
            p1.append(p1Card)
            p1.append(p2Card)
        if p2Card > p1Card:
            p2.append(p2Card)
            p2.append(p1Card)
    total = 0
    if len(p2) == 0:
        p1.reverse()
        for i, card in enumerate(p1):
            total += card * (i + 1)
    if len(p1) == 0:
        p2.reverse()
        for i, card in enumerate(p2):
            total += card * (i + 1)
    return total

def part2(p1, p2):
    return "not yet implemented"

print("Part1:", part1(p1, p2))
print("Part2:", part2(p1, p2))