import itertools
def get_pins(observed):
    possible_numbers = [[0]*5 for i in range(len(observed))]
    
    for index, number in enumerate(observed):
        number = int(number)
        if int(number) == 1:
            possible_numbers[index] = ['2', '4', '1']
        elif int(number) == 2:
            possible_numbers[index] = ['1', '3', '5', '2']
        elif int(number) == 3:
            possible_numbers[index] = ['2', '6', '3']
        elif int(number) == 4:
            possible_numbers[index] = ['1', '5', '7', '4']
        elif int(number) == 5:
            possible_numbers[index] = ['2', '4', '6', '8', '5']
        elif int(number) == 6:
            possible_numbers[index] = ['3', '5', '9', '6']
        elif int(number) == 7:
            possible_numbers[index] = ['4', '8', '7']
        elif int(number) == 8:
            possible_numbers[index] = ['5', '7', '9', '0', '8']
        elif int(number) == 9:
            possible_numbers[index] = ['6', '8', '9']
        elif int(number) == 0:
            possible_numbers[index] = ['8', '0']
    
    return [''.join(numbers) for numbers in list(itertools.product(*possible_numbers))]


'''
numbers = {
        '1': [1,4,2],
        '2': [1,2,3,5],
        '3': [2,3,6],
        '4': [1,4,5,7],
        '5': [2,4,5,6,8],
        '6': [3,5,6,9],
        '7': [4,7,8],
        '8': [0,5,7,8,9],
        '9': [6,8,9],
        '0': [0,8]
    }
possible = [numbers[x] for x in list]
'''
