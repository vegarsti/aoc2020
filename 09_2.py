with open("input/09.txt", "r") as f:
    numbers = [int(i) for i in f.readlines()]

invalid_number = 85848519
start, end = 0, 2
while end < len(numbers):
    subset = numbers[start:end]
    subset_sum = sum(subset)
    if subset_sum == invalid_number:
        print(min(subset) + max(subset))
        break
    if subset_sum < invalid_number:
        end += 1
    if subset_sum > invalid_number:
        start += 1
