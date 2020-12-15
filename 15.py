starting_numbers = [1, 2, 16, 19, 18, 0]
previously = {n: i + 1 for i, n in enumerate(starting_numbers[:-1])}
spoken = starting_numbers[-1]
turn = len(starting_numbers) - 1
for limit in (2020, 30000000):
    while (turn := turn + 1) < limit:
        previously[spoken], spoken = turn, turn - previously.get(spoken, turn)
    print(spoken)
