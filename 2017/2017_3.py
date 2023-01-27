input = 289326

size = int(input ** 0.5) + 1
center = (size - 1) // 2 + 1
print(max(0, center - 1 + abs(center - input % size)))


def next_coords(x, y):
    if x == y == 0:
        return (1, 0)
    if y > -x and x > y:
        return (x, y+1)
    if y > -x and y >= x:
        return (x-1, y)
    if y <= -x and x < y:
        return (x, y-1)
    if y <= -x and x >= y:
        return (x+1, y)


x, y = 0, 0
vals = {(0, 0): 1}
while vals[(x, y)] <= input:  # type: ignore
    x, y = next_coords(x, y)  # type: ignore
    vals[(x, y)] = sum(vals.get((x+i, y+j), 0)  # type: ignore
                       for i in [-1, 0, 1] for j in [0, 1, -1])
print(vals[(x, y)])  # type: ignore
