with open("input/08.txt", "r") as f:
    lines = f.readlines()

seen, acc, i = set(), 0, 0
while i not in seen:
    seen.add(i)
    operation, number = lines[i].split()
    sign = 2 * (number[0] == "+") - 1
    value = int(number[1:])
    if operation == "jmp":
        i += sign * value
        continue
    if operation == "acc":
        acc += sign * value
    i += 1
print(acc)
