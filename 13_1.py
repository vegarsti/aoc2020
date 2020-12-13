with open("input/13.txt", "r") as f:
    lines = f.readlines()

min_timestamp = int(lines[0])
buses = sorted(int(i) for i in lines[1].split(",") if i != "x")
timestamp = min_timestamp
while True:
    for bus in buses:
        if timestamp % bus == 0:
            print(bus * (timestamp - min_timestamp))
            exit(0)
    timestamp += 1
