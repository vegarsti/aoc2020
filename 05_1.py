with open("input/05.txt", "r") as f:
    boarding_passes = f.readlines()


def binary_representation_to_number(s: str) -> int:
    binary_s = s.replace("F", "0").replace("L", "0").replace("B", "1").replace("R", "1")
    return int(binary_s, base=2)


def seat_id(boarding_pass: str) -> int:
    row = binary_representation_to_number(boarding_pass[:7])
    column = binary_representation_to_number(boarding_pass[7:])
    return row * 8 + column


print(max(seat_id(p) for p in boarding_passes))
