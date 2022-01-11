def encode_rail_fence_cipher(string, n):
    """
    The string can be encoded by navigating the rail fence and
    appending the characters to the different dictionary positions

    "WEAREDISCOVEREDFLEEATONCE" -> WECRLTEERDSOEEFEAOCAIVDEN

    W       E       C       R       L       T       E
      E   R   D   S   O   E   E   F   E   A   O   C
        A       I       V       D       E       N

    That means the counter will go from the top to the bottom and change
    direction. We can then in the order of the dictionary add them together.
    """
    if n == 1:
        return string

    counter, dir = 0, 1
    result = []
    dictionary = {i: [] for i in range(n)}

    for i in range(len(string)):
        dictionary[counter].append(string[i])

        if counter == 0:
            dir = 1
        elif counter == n - 1:
            dir = 0

        if dir:
            counter += 1
        else:
            counter -= 1

    for value in dictionary.values():
        result.extend(value)

    return ''.join(result)


"""
This can be solved by creating a x line rail
after filling it iterate through the array to fil positions.
dic = {
    0: [x,x,x,x,x],
    1: [x,x,x,x,x,x,x,x],
    2: [x,x,x,x,x],
}

->
dic = {
    0: [a,b,c,d,e],
    1: [x,x,x,x,x,x,x,x],
    2: [x,x,x,x,x],
}

The last step is adding them to the correct position in the
result list.
"""


def decode_rail_fence_cipher(string, n):
    if n == 1:
        return string

    counter, dir = 0, 1
    result = []
    dictionary = {i: [] for i in range(n)}

    for i in range(len(string)):
        dictionary[counter].append('')

        if counter == 0:
            dir = 1
        elif counter == n - 1:
            dir = 0

        if dir:
            counter += 1
        else:
            counter -= 1

    i = 0
    for index, j in enumerate(dictionary.values()):
        new_list = []
        for _ in j:
            new_list.append(string[i])
            i += 1

        dictionary[index] = new_list

    counter, dir = 0, 1

    for _ in range(len(string)):
        result.append(dictionary[counter][0])
        dictionary[counter].pop(0)

        if counter == 0:
            dir = 1
        elif counter == n - 1:
            dir = 0

        if dir:
            counter += 1
        else:
            counter -= 1

    return ''.join(result)
