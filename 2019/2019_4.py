input = list(map(int, ("197487-673251".split("-"))))

total = 0
for number in range(input[0], input[1] + 1):
    previous = 1
    previous_previous = 1
    valid = True
    has_double = False
    for digit in str(number):
        if int(digit) < previous:
            valid = False
        if int(digit) == previous and not has_double:
            has_double = True
        if has_double and int(digit) == previous == previous_previous:
            has_double = False
        previous_previous = previous
        previous = int(digit)
    if valid and has_double:
        total += 1
print(total)
