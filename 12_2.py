with open("input/12.txt", "r") as f:
    lines = f.readlines()

east, north = 0, 0
waypoint_east, waypoint_north = 10, 1
for line in lines:
    direction, number = line[0], int(line[1:])
    if direction == "R":
        for _ in range(number // 90):
            waypoint_east, waypoint_north = waypoint_north, -waypoint_east
    if direction == "L":
        for _ in range(number // 90):
            waypoint_east, waypoint_north = -waypoint_north, waypoint_east
    if direction == "F":
        east += number * waypoint_east
        north += number * waypoint_north
    if direction == "N":
        waypoint_north += number
    if direction == "S":
        waypoint_north -= number
    if direction == "E":
        waypoint_east += number
    if direction == "W":
        waypoint_east -= number

print(abs(east) + abs(north))
