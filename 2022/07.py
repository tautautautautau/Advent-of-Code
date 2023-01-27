
# def get_dir_size(dir):
#    total = 0
#    for file in dirs[dir]:
#        if file.split(" ")[0].isnumeric():
#            total += int(file.split(" ")[0])
#        elif file.split(" ")[0] == "dir":
#            total += get_dir_size(file.split(" ")[1])
#        else:
#            print(file)
#    return total


lines = [l.strip() for l in open("input/day7.txt").readlines()]

path = root = {}
path_stack = []

file_system_size = 70000000
update_size = 30000000
sizes = []


for line in lines:
    words = line.split(" ")
    if words[0] == "$":
        if words[1] == "cd":
            if words[2] == "/":
                path = root
                path_stack = []
            elif words[2] == "..":
                path = path_stack.pop()
            else:
                if words[2] not in path:
                    path[words[2]] = {}
                path_stack.append(path)
                path = path[words[2]]
    else:
        a, b = line.split(" ")
        if a == "dir":
            if b not in path:
                path[b] = {}
        else:
            path[b] = int(a)


def solve(dir=root):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    ans = 0
    for child in dir.values():
        s, a = solve(child)
        size += s
        ans += a
    sizes.append(size)
    if size <= 100000:
        ans += size
    return (size, ans)


system_used_space, part1 = solve()
print(part1)

system_free_space = int(file_system_size) - \
    int(system_used_space)  # type: ignore
space_needed = update_size - system_free_space
sizes.sort()
for size in sizes:
    if size >= space_needed:
        print(size)
        break
