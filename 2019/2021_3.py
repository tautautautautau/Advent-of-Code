import numpy

lines = [l.strip() for l in open("2021_3.txt").readlines()]

arr = numpy.empty((len(lines[0]), len(lines)))


def get_most_common(index, array):
    ones, zeroes = 0, 0
    for elem in array:
        if elem[index] == "1":
            ones += 1
        else:
            zeroes += 1
    if zeroes > ones:
        return 0
    else:
        return 1


def get_least_common(index, array):
    ones, zeroes = 0, 0
    for elem in array:
        if elem[index] == "1":
            ones += 1
        else:
            zeroes += 1
    if zeroes > ones:
        return 1
    else:
        return 0


for i, value in zip(range(len(lines)), lines):
    for j, bit in zip(range(len(value)), value):
        arr[j][i] = int(bit)

most_common = ""
least_common = ""
for a in arr:
    most_common += str(round(numpy.average(a)))

for bit in most_common:
    if bit == "1":
        least_common += "0"
    else:
        least_common += "1"


gamma_rate = int(most_common, 2)
epsilon_rate = int(least_common, 2)
power_level = gamma_rate * epsilon_rate
print(gamma_rate, epsilon_rate, power_level)

oxygen_generator_rating = lines.copy()
for i in range(len(oxygen_generator_rating[0])):
    common = get_most_common(i, oxygen_generator_rating)
    to_remove = []
    for e in range(len(oxygen_generator_rating)):
        if oxygen_generator_rating[e][i] != str(common):
            to_remove.append(e)
    to_remove.reverse()
    for k in to_remove:
        oxygen_generator_rating.pop(k)
oxygen_generator_rating = int(oxygen_generator_rating.pop(), 2)

co2_scrubber_rating = lines.copy()
i = 0
while len(co2_scrubber_rating) != 1:
    least_common = get_least_common(i, co2_scrubber_rating)
    to_remove = []
    for e in range(len(co2_scrubber_rating)):
        if co2_scrubber_rating[e][i] != str(least_common):
            to_remove.append(e)
    to_remove.reverse()
    for k in to_remove:
        co2_scrubber_rating.pop(k)
    i += 1
co2_scrubber_rating = int(co2_scrubber_rating.pop(), 2)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(life_support_rating)
