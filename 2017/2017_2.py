with open("2017_2.txt") as file:
    lines = [l.strip() for l in file.readlines()]

a = 0
b = 0

for line in lines:
    line = sorted(list(map(int, line.split())))
    a += max(line) - min(line)
    for A in line:
        for B in line:
            if A % B == 0 and A != B:
                b += A // B

print(a)
print(b)