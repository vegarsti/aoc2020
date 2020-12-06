with open("input/06.txt", "r") as f:
    groups = ["".join(group.split("\n")).strip() for group in f.read().split("\n\n")]

print(sum(len(set(group)) for group in groups))
