def next_bigger(ns):
    numbers = [int(x) for x in str(ns)]
    k = len(numbers) - 2
    while k > 0:
        if numbers[k] < numbers[k + 1]:
            break
        k -= 1

    if k < 0:
        return -1

    for l in range(len(numbers) - 1, k, -1):
        if numbers[l] > numbers[k]:
            break

    numbers[l], numbers[k] = numbers[k], numbers[l]
    numbers[k + 1:] = reversed(numbers[k + 1:])

    return int(''.join([str(x) for x in numbers]))
    