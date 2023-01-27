with open("2018_2.txt") as file:
    lines = [l.strip() for l in file.readlines()]

twos = [0] * len(lines)
threes = [0] * len(lines)
index = 0
for line in lines:
    for letter in line:
        if line.count(letter) == 2:
            twos[index] = 1
        if line.count(letter) == 3:
            threes[index] = 1
    index += 1
print(sum(twos) * sum(threes))

for a in range(len(lines) - 1):
    for b in range(a + 1, len(lines)):
        diff = 0
        spot = 0
        for i in range(len(lines[a])):
            if lines[a][i] != lines[b][i]:
                spot = i
                diff += 1
        if diff == 1:
            print(lines[a][0:spot] + lines[a][spot+1:])