def encode_rail_fence_cipher(string, n):
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


def decode_rail_fence_cipher(string, n):
    """
    Solution solved with the help of:
    https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/
    """

    if n == 1:
        return string

    rail = [['\n' for _ in range(len(string))]
            for _ in range(n)]
    dir_down = None
    row, col = 0, 0
    index = 0
    result = []

    for _ in range(len(string)):
        if row == 0:
            dir_down = True
        if row == n - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    for i in range(n):
        for j in range(len(string)):
            if ((rail[i][j] == '*') and
               (index < len(string))):
                rail[i][j] = string[index]
                index += 1

    row, col = 0, 0
    for _ in range(len(string)):

        if row == 0:
            dir_down = True
        if row == n-1:
            dir_down = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return "".join(result)
