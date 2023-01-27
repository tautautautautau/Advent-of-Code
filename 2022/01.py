data_lines = open("input/day1.txt").readlines()
elfs = [0]
elf_index = 0
for line in data_lines:
	line = line.rstrip()
	if len(line) == 0:
		elf_index += 1
		elfs.append(0)
	else:
		elfs[elf_index] += int(line)
sorted_elfs = sorted(elfs)
total_calories = 0
for _ in range(3):
	value = sorted_elfs.pop()
	total_calories += value
	print(_ + 1, value)
print("Total", total_calories)