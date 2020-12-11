with open("input/10.txt", "r") as f:
    numbers = list(sorted(int(i) for i in f.readlines()))

diffs = [n2 - n1 for n1, n2 in zip([0] + numbers, numbers + [max(numbers) + 3])]
ones = sum(n == 1 for n in diffs)
threes = sum(n == 3 for n in diffs)
print(ones * threes)
