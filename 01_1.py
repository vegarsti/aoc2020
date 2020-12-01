with open("input/1.txt", "r") as f:
    numbers = [int(line) for line in f.readlines()]

for _, number1 in enumerate(numbers):
    for _, number2 in enumerate(numbers):
        if number1 + number2 == 2020:
            print(number1 * number2)
            exit(0)

exit(1)
