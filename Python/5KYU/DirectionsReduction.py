# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def dirReduc(arr):
    index = 0
    while index < len(arr) - 1:
        if((arr[index] == 'NORTH' and arr[index + 1] == 'SOUTH') or
           (arr[index] == 'SOUTH' and arr[index + 1] == 'NORTH') or
           (arr[index] == 'EAST' and arr[index + 1] == 'WEST') or
           (arr[index] == 'WEST' and arr[index + 1] == 'EAST')):
            del arr[index + 1]
            del arr[index]
            index = -1
        index += 1
        
    return arr
