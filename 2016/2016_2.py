with open("2016_2.txt") as file:
    lines = [l.strip() for l in file.readlines()]

kpad = [[" ", " ", "1", " ", " "],
        [" ", "2", "3", "4", " "],
        ["5", "6", "7", "8", "9"],
        [" ", "A", "B", "C", " "],
        [" ", " ", "D", " ", " "],]

location = [2, 0]
code = ""

for instructions in lines:
    for instruction in list(instructions):
        if instruction == "U":
            if location[0]-1 >= 0:
                if kpad[location[0]-1][location[1]] != " ":
                    location[0] -= 1
        if instruction == "D":
            if location[0]+1 <= 4:
                if kpad[location[0]+1][location[1]] != " ":
                    location[0] += 1
        if instruction == "L":
            if location[1]-1 >= 0:
                if kpad[location[0]][location[1]-1] != " ":
                    location[1] -= 1
        if instruction == "R":
            if location[1]+1 <= 4:
                if kpad[location[0]][location[1]+1] != " ":
                    location[1] += 1
    code += kpad[location[0]][location[1]]

print(code)
