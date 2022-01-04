def high_and_low(numbers):
    numbers = sorted([int(i) for i in numbers.split()])
    return str(numbers[-1]) + " " + str(numbers[0])
