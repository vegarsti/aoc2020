from typing import List

with open("input/06_test.txt", "r") as f:
    groups = [group.split("\n") for group in f.read().split("\n\n")]


def everyone(answers: List[str]) -> int:
    intersection = set(answers[0]).intersection(*(set(answer) for answer in answers[1:]))
    return len(intersection)


print(sum(everyone(a) for a in groups))
