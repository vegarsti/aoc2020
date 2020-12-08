with open("input/08.txt", "r") as f:
    lines = f.readlines()

for instruction, _ in enumerate(lines):
    seen, acc, i = set(), 0, 0
    while i not in seen and i < len(lines):
        seen.add(i)
        operation, number = lines[i].split()
        sign = 2 * (number[0] == "+") - 1
        value = int(number[1:])
        if i == instruction and operation in {"nop", "jmp"}:
            operation = {"nop": "jmp", "jmp": "nop"}[operation]
        if operation == "jmp":
            i += sign * value
            continue
        if operation == "acc":
            acc += sign * value
        i += 1
    if i == len(lines):
        print(acc)
