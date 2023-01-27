lines = [l.strip() for l in open("input/day10.txt").readlines()]

x = 1
line = 0
processing = 0
amount = 0
total = 0
pixels = ""

for cycle in range(240):
    total += cycle * x if cycle in [20, 60, 100, 140, 180, 220] else 0
    if processing == 0:
        x += amount
        amount = 0
        if "addx" in lines[line] and not processing:
            processing = 1
            amount = int(lines[line].split()[1])
        line += 1
    else:
        processing -= 1

    pixels += "\n" if cycle % 40 == 0 else ""
    pixels += "█" if cycle % 40 in [x-1, x, x+1] else "░"

print(total)
print(pixels)
