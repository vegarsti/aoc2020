import itertools
from typing import List

with open("input/09.txt", "r") as f:
    numbers = [int(i) for i in f.readlines()]


def sums_to(nums: List[int], n: int) -> bool:
    seen = set()
    for x, y in itertools.product(nums, nums):
        x, y = tuple(sorted((x, y)))
        if x == y or (x, y) in seen:
            continue
        seen.add((x, y))
        if n == x + y:
            return True
    return False


preamble_length = 25
for i, number in enumerate(numbers):
    if i < preamble_length:
        continue
    start = max(0, i - preamble_length)
    subset = numbers[start:i]
    if not sums_to(subset, number):
        print(number)
        break
