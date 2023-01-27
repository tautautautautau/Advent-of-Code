import os
import time


lines = [l.strip() for l in open("input/day14.txt").readlines()]
test = ["498,4 -> 498,6 -> 496,6",
        "503,4 -> 502,4 -> 502,9 -> 494,9"]

walls = []
lowest_x, lowest_y = float('inf'), float('inf')
highest_x, highest_y = float('-inf'), float('-inf')

for line in lines:
    coords = line.split(" -> ")
    x, y = None, None
    prev_x, prev_y = None, None
    for coord in coords:
        prev_x, prev_y = x, y
        x, y = map(int, coord.split(","))
        if x > highest_x:
            highest_x = x
        if y > highest_y:
            highest_y = y
        if x < lowest_x:
            lowest_x = x
        if y < lowest_y:
            lowest_y = y
        if prev_x != None and prev_y != None:
            if prev_x == x:
                lower = min(y, prev_y)
                higher = max(y, prev_y)
                for j in range(lower, higher + 1):
                    walls.append([x, j])
            if prev_y == y:
                lower = min(x, prev_x)
                higher = max(x, prev_x)
                for i in range(lower, higher + 1):
                    walls.append([i, y])

padding = 2
highest_x, lowest_x = int(highest_x) + padding, int(lowest_x) - padding
highest_y, lowest_y = int(highest_y) + padding, int(lowest_y) - padding

width = (highest_x + 1) * 2
height = highest_y + 1

grid = [["." for _ in range(width)] for _ in range(height)]
floor_y = highest_y
for x in range(width):
    grid[floor_y][x] = "#"
for x, y in walls:
    grid[y][x] = "#"
grid[0][500] = "+"


def draw():
    os.system("clear")
    for row in grid:
        print("".join(row))
    time.sleep(0.1)


class Sand:
    x = 500
    y = 0


part1 = True
sand = Sand()
grains = 0
while True:
    old_sand = [sand.x, sand.y]
    grid[sand.y][sand.x] = "o"
    #draw()
    if sand.y + 1 >= highest_y and part1:
        part1 = False
        print("Sand fell to void")
        print("Total sand grains:", grains)
    if grid[sand.y + 1][sand.x] == ".":
        sand.y += 1
        grid[old_sand[1]][old_sand[0]] = "."
    elif grid[sand.y + 1][sand.x - 1] == ".":
        sand.y += 1
        sand.x -= 1
        grid[old_sand[1]][old_sand[0]] = "."
    elif grid[sand.y + 1][sand.x + 1] == ".":
        sand.y += 1
        sand.x += 1
        grid[old_sand[1]][old_sand[0]] = "."
    else:
        grains += 1
        if sand.y == 0:
            print("Sand at the top")
            print("Total sand grains:", grains)
            exit(0)
        sand = Sand()
