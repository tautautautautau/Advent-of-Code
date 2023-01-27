lines = [l.strip() for l in open("2017_4.txt").readlines()]

valid_a = 0
valid_b = 0
for line in lines:
    words = line.split()
    # part 1
    if len(words) == len(set(words)):
        valid_a += 1
    # part 2
    sorted_words = []
    for word in words:
        sorted_words.append("".join(sorted(word)))
    if len(sorted_words) == len(set(sorted_words)):
        valid_b += 1
print(valid_a, valid_b)
