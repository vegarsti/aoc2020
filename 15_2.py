*starting_numbers, spoken = [1, 2, 16, 19, 18, 0]
previously = {n: i + 1 for i, n in enumerate(starting_numbers)}
turn = len(starting_numbers)
while (turn := turn + 1) < 30000000:
    previously[spoken], spoken = turn, turn - previously.get(spoken, turn)
print(spoken)
