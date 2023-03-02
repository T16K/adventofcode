import os

sizes = {}
stack = []

with open("input") as f:
    commands = f.readlines()

for command in commands:
    if command.startswith("$ ls") or command.startswith("dir"):
        continue
    if command.startswith("$ cd"):
        dest = command.split()[2]
        if dest == "..":
            stack.pop()
        else:
            path = os.path.join(stack[-1], dest) if stack else dest
            stack.append(path)
    else:
        size, file = command.split()
        for path in stack:
            sizes[path] = sizes.get(path, 0) + int(size)

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    if size > needed_size:
        break

print(size)
