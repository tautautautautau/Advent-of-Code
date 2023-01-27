data = [l.strip() for l in open("input/day6.txt").read()]

length = 14  # part1: 4 | part2: 14

index = 0
while len(set(data[index:index + length])) != length:
    index += 1

print(index + length)
