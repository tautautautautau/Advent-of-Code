lines = [l.strip() for l in open("input/day9.txt").readlines()]


class KNOT:
    def __init__(self, number, position):
        self.number = number
        self.position = position
        self.visited = set()
        self.visited.add(str(self.position))


def update(head, tail):
    d = ((head.position[0] - tail.position[0])
         ** 2 + (head.position[1] - tail.position[1]) ** 2) ** 0.5
    if d > 1.5:
        if head.position[0] == tail.position[0]:
            if head.position[1] > tail.position[1]:
                tail.position[1] += 1
            else:
                tail.position[1] -= 1
        elif head.position[1] == tail.position[1]:
            if head.position[0] > tail.position[0]:
                tail.position[0] += 1
            else:
                tail.position[0] -= 1
        elif head.position[0] > tail.position[0]:
            tail.position[0] += 1
            if head.position[1] > tail.position[1]:
                tail.position[1] += 1
            if head.position[1] < tail.position[1]:
                tail.position[1] -= 1
        elif head.position[0] < tail.position[0]:
            tail.position[0] -= 1
            if head.position[1] > tail.position[1]:
                tail.position[1] += 1
            if head.position[1] < tail.position[1]:
                tail.position[1] -= 1
        tail.visited.add(str(tail.position))


knots = list()
for i in range(10):
    knots.append(KNOT(i, [0, 0]))

for line in lines:
    direction, amount = line.split()
    amount = int(amount)
    vectors = {"U": [0, 1], "D": [0, -1],
               "L": [-1, 0], "R": [1, 0]}
    dir_vector = vectors[direction]
    prev_knot = None
    for _ in range(amount):
        for knot in knots:
            if knot.number == 0:
                knot.position = [knot.position[0] + dir_vector[0],
                                 knot.position[1] + dir_vector[1]]
            else:
                update(prev_knot, knot)
            prev_knot = knot

print(len(knots.pop().visited))
