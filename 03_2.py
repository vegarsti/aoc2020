import math
from typing import List


def traverse(lines: List[str], right: int, down: int) -> str:
    x, y, path = 0, 0, ""
    m, n = len(lines), len(lines[0])
    while y < m:
        path += lines[y][x]
        x = (x + right) % n
        y += down
    return path


def main() -> None:
    with open("input/03.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    scenarios = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    trees = (traverse(lines, right, down).count("#") for right, down in scenarios)
    print(math.prod(trees))


if __name__ == "__main__":
    main()
