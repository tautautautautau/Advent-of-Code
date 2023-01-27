import math

with open("2018_1.txt") as file:
    lines = [l.strip() for l in file.readlines()]

print(sum(map(int, lines)))

duplicate = math.inf
current_frequency = 0
frequencies = []
i = 0
while duplicate == math.inf:
    if i >= len(lines):
        i = 0
    current_frequency += int(lines[i])
    if current_frequency in frequencies:
        duplicate = current_frequency
    frequencies.append(current_frequency)
    i += 1
print(duplicate)