from typing import List


def visible_seats(grd: List[List[str]], i: int, j: int) -> List[str]:
    step_changes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    seats = []
    for i_diff, j_diff in step_changes:
        ii, jj = i, j
        while True:
            ii, jj = ii + i_diff, jj + j_diff
            if not (0 <= ii < len(grd) and 0 <= jj < len(grd[0])):
                break
            seats.append(grd[ii][jj])
            if grd[ii][jj] != ".":
                break
    return seats


def step(grd: List[List[str]]) -> List[List[str]]:
    new_grd = [list(i) for i in grd]
    for i, row in enumerate(grd):
        for j, seat in enumerate(row):
            occupied_seats = visible_seats(grd, i, j).count("#")
            if seat == "L" and occupied_seats == 0:
                new_grd[i][j] = "#"
            if seat == "#" and occupied_seats >= 5:
                new_grd[i][j] = "L"
    return new_grd


def grid_string(grd: List[List[str]]) -> str:
    return "\n".join("".join(row) for row in grd)


def main() -> None:
    with open("input/11.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    while (new_grid := step(grid)) != grid:
        grid = new_grid
    print(grid_string(new_grid).count("#"))


if __name__ == "__main__":
    main()
