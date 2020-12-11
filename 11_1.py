from typing import List


def adjacent_seats(grd: List[List[str]], i: int, j: int) -> List[str]:
    i_from, i_to = max(i - 1, 0), min(len(grd), i + 2)
    j_from, j_to = max(j - 1, 0), min(len(grd[0]), j + 2)
    seats = []
    for ii in range(i_from, i_to):
        for jj in range(j_from, j_to):
            if ii == i and jj == j:
                continue
            seats.append(grd[ii][jj])
    return seats


def step(grd: List[List[str]]) -> List[List[str]]:
    new_grd = [list(i) for i in grd]
    for i, row in enumerate(grd):
        for j, seat in enumerate(row):
            occupied_seats = adjacent_seats(grd, i, j).count("#")
            if seat == "L" and occupied_seats == 0:
                new_grd[i][j] = "#"
            if seat == "#" and occupied_seats >= 4:
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
