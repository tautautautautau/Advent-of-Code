import numpy

lines = [l.strip() for l in open("2018_3.txt").readlines()]

fabric = numpy.zeros((1000, 1000))

for line in lines:
    id, rest = line.split("@")
    start, size = rest.split(":")
    start_x, start_y = start.split(",")
    size_x, size_y = size.split("x")
    for x in range(int(start_x), int(start_x) + int(size_x)):
        for y in range(int(start_y), int(start_y) + int(size_y)):
            fabric[x][y] += 1

total = 0
for a in fabric.flat:
    if a >= 2:
        total += 1
print(total)

ids = []
for line in lines:
    id, rest = line.split("@")
    start, size = rest.split(":")
    start_x, start_y = start.split(",")
    size_x, size_y = size.split("x")
    overlaps = False
    for x in range(int(start_x), int(start_x) + int(size_x)):
        for y in range(int(start_y), int(start_y) + int(size_y)):
            if fabric[x][y] > 1:
                overlaps = True
    if not overlaps:
        ids.append(id)
print(ids)
