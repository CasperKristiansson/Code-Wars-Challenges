# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python
# Based on https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers

def parse_int(string):
    
    string = string.replace(' and ', ' ').replace('-', ' ').split()

    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    scales = ["hundred", "thousand", "million", "billion", "trillion"]
    
    numwords = {}
    
    for index, word in enumerate(units):
        numwords[word] = (1, index)
    for index, word in enumerate(tens):
        numwords[word] = (1, index * 10)
    for index, word in enumerate(scales):
        numwords[word] = (10 ** (index * 3 or 2), 0)

    current = result = 0
    
    for word in string:
        scale, increment = numwords[word]

        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

# Not working, Problem: 6 100 66 1000 = 666,000

def parse_int(string):
    print(string)
    string = string.replace(' and ', ' ').split()
    print(string)
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
    ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["hundred", "thousand", "million", "billion", "trillion"]
    result = []

    for index, number in enumerate(string):
        if '-' in number:
            numbers = number.split('-')
            i = 0
            while i < len(tens):
                if tens[i] == numbers[0]:
                    numbers[0] = i * 10
                i += 1
            i = 0
            while i < len(units):
                if units[i] == numbers[1]:
                    numbers[1] = i
                i += 1
            string[index] = int(numbers[0]) + int(numbers[1])
            
    print(string)
    for number in string:
        if type(number) == int:
            result.append(number)
            continue
        i, j, k = 0, 0, 0
        found = False
        while i < len(units) and not found:
            if units[i] == number:
                found = True
                result.append(i)
            i += 1
        while j < len(tens) and not found:
            if tens[j] == number:
                found = True
                result.append(j * 10)
            j += 1
        while k < len(scales) and not found:
            if scales[k] == number:
                found = True
                result.append(10 ** (k * 3 or 2))
            k += 1
    new_result = []
    i = 0
    print(result)
    
    while i < len(result):
        
        if i < len(result) - 1 and result[i] < result[i + 1]:
            new_result.append(result[i] * result[i + 1])
            i += 1
        else:
            new_result.append(result[i])
        i += 1
    sum = 0
    
    print(new_result)
    for number in new_result:
        sum += number
        
    return sum
