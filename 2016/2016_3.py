with open("2016_3.txt") as file:
    lines = [l.strip() for l in file.readlines()]

total = 0
for line in lines:
    sides = sorted(list(map(int, line.split())))
    if sides[0] + sides[1] > sides[2]:
        total += 1
print(total)

total = 0
for index in range(0, len(lines), 3):
    line1 = list(map(int, lines[index].split()))
    line2 = list(map(int, lines[index + 1].split()))
    line3 = list(map(int, lines[index + 2].split()))
    sides1 = sorted([line1[0], line2[0], line3[0]])
    sides2 = sorted([line1[1], line2[1], line3[1]])
    sides3 = sorted([line1[2], line2[2], line3[2]])
    if sides1[0] + sides1[1] > sides1[2]:
        total += 1
    if sides2[0] + sides2[1] > sides2[2]:
        total += 1
    if sides3[0] + sides3[1] > sides3[2]:
        total += 1
print(total)