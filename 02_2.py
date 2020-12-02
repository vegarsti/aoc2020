with open("input/02.txt", "r") as f:
    lines = f.readlines()


def xor(b1: bool, b2: bool) -> bool:
    return b1 != b2


def valid_line(line: str) -> bool:
    positions, letter_with_colon, password = line.split()
    letter = letter_with_colon[0]
    pos1, pos2 = positions.split("-")
    index1, index2 = int(pos1) - 1, int(pos2) - 1
    return xor(password[index1] == letter, password[index2] == letter)


print(sum(valid_line(line) for line in lines))
