import string

lines = [l.strip() for l in open("input/day3.txt").readlines()]

total = 0
for line in lines:
    a, b = line[:len(line)//2], line[len(line)//2:]
    letter = set(a).intersection(set(b)).pop()
    total += string.ascii_letters.index(letter) + 1
print(total)

total = 0
for index in range(0, len(lines), 3):
    a, b, c = lines[index], lines[index + 1], lines[index + 2]
    letter = set(a).intersection(set(b)).intersection(set(c)).pop()
    total += string.ascii_letters.index(letter) + 1
print(total)
