with open("input/08.txt", "r") as f:
    lines = f.readlines()

seen, acc, i = set(), 0, 0
while i not in seen:
    seen.add(i)
    operation, number = lines[i].split()
    if operation == "jmp":
        i += int(number)
        continue
    if operation == "acc":
        acc += int(number)
    i += 1
print(acc)
