# https://www.codewars.com/kata/52ec24228a515e620b0005ef

def exp_sum(n):
    numbers = [1] + [0] * n
    
    for j in range(1, n + 1):
        for i, x in enumerate(range(j, n + 1)):
            numbers[x] += numbers[i]

    return numbers[n]

def partition(number):
    answer = {(number, )}
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer

print(exp_sum(10))
