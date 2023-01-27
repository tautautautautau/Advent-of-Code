lines = [l.strip() for l in open("old/2015_5.txt").readlines()]

vowels = "aeiou"
prohibited = ["ab",
              "cd",
              "pq",
              "xy"]


def vowels_amount(string):
    return sum([string.count(c) for c in vowels])


def contains_double(string):
    return any(c1 == c2 for c1, c2 in zip(string, string[1:]))


def prohibited_strings(string):
    return [ele for ele in prohibited if (ele in string)]


def contains_nonoverlapping_pair(s):
    # Loop through the string and check if each pair of letters appears again later in the string
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair in s[i+2:]:
            return True
    return False


# This function returns True if the input string contains
# at least one letter which repeats with exactly one letter
# between them, and False otherwise.
def has_repeating_letter_with_one_between(s: str) -> bool:
    # Loop through the string and check for each letter
    # if it repeats with exactly one letter between them.
    for i in range(len(s) - 2):
        # Get the current letter and the two letters that follow it.
        letter = s[i]
        next_letter = s[i + 1]
        next_next_letter = s[i + 2]

        # Check if the current letter repeats with exactly one letter between them.
        if letter == next_next_letter and next_letter != letter:
            # If the current letter repeats with exactly one letter between them,
            # return True.
            return True

    # If we didn't find any letter that repeats with exactly one letter between them,
    # return False.
    return False


total = 0
for line in lines:
    if vowels_amount(line) >= 3 and contains_double(line) and len(prohibited_strings(line)) == 0:
        total += 1
print(total)

total = 0
for line in lines:
    if contains_nonoverlapping_pair(line) and has_repeating_letter_with_one_between(line):
        total += 1
print(total)
