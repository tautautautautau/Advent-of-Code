import math

data = open("2016_1.txt", "r").readline().split(", ")
x = 0
y = 0
d = "North"
coords = []
first = []
for instruction in data:
    if instruction[0] == "R":
        if d == "North":
            for _ in range(int(instruction[1:])):
                x += 1
                if [x, y] in coords:
                    if first == []:
                        first = [x, y]
                coords.append([x, y])
            d = "East"
            continue
        if d == "East":
            for _ in range(int(instruction[1:])):
                y -= 1
                if [x, y] in coords:
                    if first == []:
                        first = [x, y]
                coords.append([x, y])
            d = "South"
            continue
        if d == "South":
            for _ in range(int(instruction[1:])):
                x -= 1
                if [x, y] in coords:
                    if first == []:
                        first = [x, y]
                coords.append([x, y])
            d = "West"
            continue
        if d == "West":
            for _ in range(int(instruction[1:])):
                y += 1
                if [x, y] in coords:
                    if first == []:
                        first = [x, y]
                coords.append([x, y])
            d = "North"
            continue
    if instruction[0] == "L":
        if d == "North":
            for _ in range(int(instruction[1:])):
                x -= 1
                if [x, y] in coords:
                    if first == []:
                        first = [x, y]
                coords.append([x, y])
            d = "West"
            continue
        if d == "East":
            for _ in range(int(instruction[1:])):
                y += 1
                if [x, y] in coords:
                    if first == []:
                        first = [x, y]
                coords.append([x, y])
            d = "North"
            continue
        if d == "South":
            for _ in range(int(instruction[1:])):
                x += 1
                if [x, y] in coords:
                    if first == []:
                        first = [x, y]
                coords.append([x, y])
            d = "East"
            continue
        if d == "West":
            for _ in range(int(instruction[1:])):
                y -= 1
                if [x, y] in coords:
                    if first == []:
                        first = [x, y]
                coords.append([x, y])
            d = "South"
            continue
print(abs(x) + abs(y))
print(abs(first[0]) + abs(first[1]))
#print(coords)
