lines = [l.strip() for l in open("input/day4.txt").readlines()]

subsets = 0
intersections = 0
for line in lines:
    first = list(map(int, (line[:line.index(",")]).split("-")))
    second = list(map(int, (line[line.index(",") + 1:]).split("-")))
    first = set([*range(first[0], first[1] + 1)])
    second = set([*range(second[0], second[1] + 1)])
    if first.issubset(second) or second.issubset(first):
        subsets += 1
    if len(first.intersection(second)) > 0:
        intersections += 1
print(subsets, intersections)
