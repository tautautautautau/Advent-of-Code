with open("input/day2.txt") as file:
    lines = [l.strip() for l in file.readlines()]

WIN = 6
TIE = 3
LOSS = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

R = "A"
P = "B"
S = "C"

score = 0
rounds = 0
for round in lines:
    opponent, outcome = round.split(" ")
    if opponent == R:
        if outcome == "X":
            score += LOSS + SCISSORS
        if outcome == "Y":
            score += TIE + ROCK
        if outcome == "Z":
            score += WIN + PAPER
    if opponent == P:
        if outcome == "X":
            score += LOSS + ROCK
        if outcome == "Y":
            score += TIE + PAPER
        if outcome == "Z":
            score += WIN + SCISSORS
    if opponent == S:
        if outcome == "X":
            score += LOSS + PAPER
        if outcome == "Y":
            score += TIE + SCISSORS
        if outcome == "Z":
            score += WIN + ROCK
    print(score)