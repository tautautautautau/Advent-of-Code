with open("2017_1.txt") as file:
    lines = [l.strip() for l in file.readlines()]

digits = list(lines[0])
steps = int(len(digits)/2)

total = 0
for i in range(len(digits)):
    j = i + 1
    if j >= len(digits):
        j = 0
    if digits[i] == digits[j]:
        total += int(digits[i])
print(total)

total = 0
for i in range(len(digits)):
    j = i + steps
    if j >= len(digits):
        j -= len(digits)
    if digits[i] == digits[j]:
        total += int(digits[i])
print(total)