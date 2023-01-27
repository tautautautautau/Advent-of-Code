import re
import string

lines = [l.strip() for l in open("2016_4.txt").readlines()]

total = 0
for line in lines:
    id = re.findall(r"\d+", line)[0]
    letter_groups = re.findall(r"[a-z]+", line)
    checksum = letter_groups.pop()
    # part 1
    letters = "".join(letter_groups)
    letters_dict = {}
    for letter in letters:
        if letters_dict.get(letter):
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    sorted_alphabetical = dict(sorted(letters_dict.items()))
    sorted_values = dict(
        sorted(sorted_alphabetical.items(), key=lambda item: item[1], reverse=True))
    top_five_letters = "".join(list(sorted_values.keys())[:5])
    if top_five_letters == checksum:
        total += int(id)
    # part 2
    word = ""
    for letter in letters:
        word += string.ascii_lowercase[(string.ascii_lowercase.index(
            letter) + int(id)) % len(string.ascii_lowercase)]
    if "northpoleobjects" in word:
        print(id, word)
print(total)
