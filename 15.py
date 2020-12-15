from collections import defaultdict

starting_numbers = [1, 2, 16, 19, 18, 0]
history = defaultdict(list)
for i, n in enumerate(starting_numbers):
    history[n].append(i)
spoken = starting_numbers[-1]
turn = len(starting_numbers) - 1
for limit in (2020, 30000000):
    while (turn := turn + 1) < limit:
        spoken = history[spoken][-1] - history[spoken][-2] if len(history[spoken]) > 1 else 0
        history[spoken].append(turn)
    print(spoken)
    turn -= 1
