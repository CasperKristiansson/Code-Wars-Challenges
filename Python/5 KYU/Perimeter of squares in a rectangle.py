# https://www.codewars.com/kata/559a28007caad2ac4e000083/train/python

def perimeter(n):
    first, second, sum = 0, 1, 1
    for _ in range(n):
        first, second = second, first + second
        sum += second

    return sum * 4
