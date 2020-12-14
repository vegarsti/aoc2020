def solve_congruence(a: int, b: int, m: int) -> int:
    x = 0
    while (a * x) % m != b:
        x += 1
    return x


with open("input/13.txt", "r") as f:
    lines = f.readlines()
buses = sorted(((i, int(s)) for i, s in enumerate(lines[1].strip().split(",")) if s != "x"))
total_offset, step_length = buses[0]
for offset, next_step in buses[1:]:
    remainder = (next_step - offset - total_offset) % next_step
    steps = solve_congruence(a=step_length, b=remainder, m=next_step)
    total_offset += step_length * steps
    step_length *= next_step
print(total_offset)
