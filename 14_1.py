from typing import List

with open("input/14.txt", "r") as f:
    lines = f.readlines()

groups_of_lines: List[List[str]] = []
batch: List[str] = []
for i, line in enumerate(lines):
    if i > 0 and line.startswith("mask"):
        groups_of_lines.append(batch)
        batch = []
    batch.append(line.strip())
groups_of_lines.append(batch)

memory = {}
for lines in groups_of_lines:
    mask = [(i, int(s)) for i, s in enumerate(reversed(lines[0].strip().split("mask = ")[1])) if s != "X"]
    for line in lines[1:]:
        address, number = (int(i) for i in line[4:].strip().split("] = "))
        bin_number = list(reversed(list("0" * (36 - len(bin(number)[2:])) + bin(number)[2:])))
        for i, n in mask:
            bin_number[i] = str(n)
        number = int(f"0b{''.join(reversed(bin_number))}", 2)
        memory[address] = number

print(sum(memory.values()))
