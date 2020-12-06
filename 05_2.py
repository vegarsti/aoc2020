with open("input/05.txt", "r") as f:
    boarding_passes = f.readlines()


def to_number(s: str, zero: str, one: str) -> int:
    binary_s = s.replace(zero, "0").replace(one, "1")
    return int(binary_s, base=2)


def seat_id(boarding_pass: str) -> int:
    row = to_number(boarding_pass[:7], zero="F", one="B")
    column = to_number(boarding_pass[7:], zero="L", one="R")
    return row * 8 + column


seat_ids = list(sorted(seat_id(p) for p in boarding_passes))
seat_id_diffs = ((next_sid - sid, sid) for sid, next_sid in zip(seat_ids, seat_ids[1:]))
for diff, sid in seat_id_diffs:
    next_seat_is_missing = diff == 2
    if next_seat_is_missing:
        next_seat = sid + 1
        print(next_seat)
