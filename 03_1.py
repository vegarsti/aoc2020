with open("input/03.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

x, path = 0, ""
n = len(lines[0])
for _, line in enumerate(lines):
    path += line[x]
    x = (x + 3) % n
print(path.count("#"))
