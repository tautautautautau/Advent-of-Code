lines = [l.strip() for l in open("input/input.txt").readlines()]
#lines = [l.strip() for l in open("input/test_input.txt").readlines()]


def check_directions(obsidian, directions) -> bool():
    got_to_edge = True
    for direction in directions:
        pts = obsidian
        while min(pts) >= min_max[0] and max(pts) <= min_max[1]:
            if pts in coords:
                got_to_edge = False
            pts = [*map(sum, zip(pts, direction))]
    return got_to_edge


def check_neighbors(obsidian) -> int():
    sides = 0
    outside = 0
    directions = [[1, 0, 0], [-1, 0, 0],
                  [0, 1, 0], [0, -1, 0],
                  [0, 0, 1], [0, 0, -1]]
    out = False
    for direction in directions:
        neighbor = [*map(sum, zip(obsidian, direction))]
        if neighbor not in coords:
            sides += 1
        if check_directions(neighbor, directions):
            outside += 1
    return sides, sides - outside


def find_outmost_values(coords) -> tuple():
    lowest = float('inf')
    highest = float('-inf')
    for coord in coords:
        mx = max(coord)
        mn = min(coord)
        if mx > highest:
            highest = mx
        if mn < lowest:
            lowest = mn
    return (lowest, highest)


coords = list()
for line in lines:
    line = line.split(",")
    coords.append([int(line[0]), int(line[1]), int(line[2])])


min_max = find_outmost_values(coords)

total_sides_visible = 0
outside_area = 0
for obsidian in coords:
    tmp = check_neighbors(obsidian)
    total_sides_visible += tmp[0]
    outside_area += tmp[1]
print(total_sides_visible, outside_area)
