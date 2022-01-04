def square_digits(num):
    return int(''.join([str(int(number) ** 2) for number in str(num)]))
    