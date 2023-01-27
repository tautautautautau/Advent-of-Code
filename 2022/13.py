import functools


pairs = open("input/day13.txt").read().split("\n\n")
lines = [l.strip() for l in open("input/day13.txt").readlines()]


def compare(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    if type(a) == int and type(b) == list:
        return compare([a], b)
    if type(a) == list and type(b) == int:
        return compare(a, [b])
    if type(a) == list and type(b) == list:
        if len(a) == len(b):
            for aa, bb in zip(a, b):
                c = compare(aa, bb)
                if c != 0:
                    return c
            return 0
        else:
            for i in range(min(len(a), len(b))):
                aa = a[i]
                bb = b[i]
                c = compare(aa, bb)
                if c != 0:
                    return c
            if len(a) < len(b):
                return -1
            else:
                return 1
    return 0


all = []
answer = 0
for num, pair in enumerate(pairs):
    left, right = pair.split("\n")
    left = eval(left.rstrip())
    right = eval(right.rstrip())
    if compare(left, right) < 0:
        answer += num + 1
    all.extend([left, right])
print(answer)

all.append([2])
all.append([6])
new = sorted(all, key=functools.cmp_to_key(compare))
print((new.index([2]) + 1) * (new.index([6]) + 1))
