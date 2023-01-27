trees = [l.strip() for l in open("input/day8.txt").readlines()]
total, scenic = 0, 0
for y in range(len(trees)):
    for x in range(len(trees[y])):
        up, down, left, right = True, True, True, True
        scenic_points = [0, 0, 0, 0]
        for y_pointer in reversed(range(y)):
            scenic_points[0] += 1
            if trees[y_pointer][x] >= trees[y][x]:
                up = False
                break
        for y_pointer in range(y+1, len(trees)):
            scenic_points[1] += 1
            if trees[y_pointer][x] >= trees[y][x]:
                down = False
                break
        for x_pointer in reversed(range(x)):
            scenic_points[2] += 1
            if trees[y][x_pointer] >= trees[y][x]:
                left = False
                break
        for x_pointer in range(x+1, len(trees)):
            scenic_points[3] += 1
            if trees[y][x_pointer] >= trees[y][x]:
                right = False
                break
        total += 1 if any([up, down, left, right]) else 0
        if eval('*'.join(map(str, scenic_points))) > scenic:
            scenic = eval('*'.join(map(str, scenic_points)))
print(total, scenic)
