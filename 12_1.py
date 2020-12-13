with open("input/12.txt", "r") as f:
    lines = f.readlines()

directions, facing = ("E", "S", "W", "N"), 0
east, north = 0, 0
for line in lines:
    direction, number = line[0], int(line[1:])
    if direction == "R":
        facing = (facing + number // 90) % 4
    if direction == "L":
        facing = (facing - number // 90) % 4
    if direction == "F":
        direction = directions[facing]
    if direction == "N":
        north += number
    if direction == "S":
        north -= number
    if direction == "E":
        east += number
    if direction == "W":
        east -= number

print(abs(east) + abs(north))
