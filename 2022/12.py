grid = [list(l.strip()) for l in open("input/day12.txt").readlines()]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
test_grid = [list("Sabqponm"), list("abcryxxl"), list(
    "accszExk"), list("acctuvwj"), list("abdefghi")]


def find_start_end_letter(grid, letter):
    start, end, letters = None, None, list()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                start = (x, y)
                grid[y][x] = "a"
            if grid[y][x] == "E":
                end = (x, y)
                grid[y][x] = "z"
            if grid[y][x] == letter:
                letters.append((x, y))
    return start, end, letters, grid


def valid_move(a, b, grid, part):
    x1, y1 = a
    new_x, new_y = b
    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
        start_letter = grid[y1][x1]
        destination_letter = grid[new_y][new_x]
        if part == 1:
            return True if ord(destination_letter) - ord(start_letter) < 2 else False
        if part == 2:
            return True if ord(start_letter) - ord(destination_letter) < 2 else False
    return False


def find_shortest_length(grid, start, end, part):
    start_x, start_y = start
    length = 0
    visited = set()
    queue = list()
    queue.append((start_x, start_y, 0))
    while queue:
        x, y, length = queue.pop(0)
        if (x, y) == end or (x, y) in end:
            return length
        visited.add((x, y))
        for move in moves:
            move_x, move_y = move
            new_x, new_y = x + move_x, y + move_y
            if (x, y, length) not in queue:
                if (new_x, new_y) not in visited:
                    if valid_move((x, y), (new_x, new_y), grid, part):
                        queue.append((new_x, new_y, length + 1))
    return -1


# Test
# start, end, letters, grid = find_start_end_letter(test_grid, 'a')
start, end, letters, grid = find_start_end_letter(grid, 'a')

# part 1
print(find_shortest_length(grid, start, end, 1))

# part 2
print(find_shortest_length(grid, end, letters, 2))
