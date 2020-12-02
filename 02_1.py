with open("input/02.txt", "r") as f:
    lines = f.readlines()


def valid_line(line: str) -> bool:
    minmax, letter_with_colon, password = line.split()
    letter = letter_with_colon[0]
    min_, max_ = minmax.split("-")
    counts = password.count(letter)
    if int(min_) <= counts <= int(max_):
        return True
    return False


print(sum(valid_line(line) for line in lines))
