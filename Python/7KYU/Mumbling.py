def accum(s):
    string = ''
    for index, letter in enumerate(s):
        string += letter.upper()
        for _ in range(index):
            string += letter.lower()
        string += '-'
    return string[:-1]