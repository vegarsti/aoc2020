with open("input/01.txt", "r") as f:
    numbers = [int(line) for line in f.readlines()]

for number1 in numbers:
    for number2 in numbers:
        for number3 in numbers:
            if number1 + number2 + number3 == 2020:
                print(number1 * number2 * number3)
                exit(0)

exit(1)
