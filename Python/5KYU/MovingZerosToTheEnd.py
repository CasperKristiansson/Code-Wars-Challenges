def move_zeros(array):
    i = 0
    j = len(array) - 1
    while i < len(array):
        if array[i] == 0 and i < j:
            array.append(array.pop(i))
            j -= 1
        else:
            i += 1
            
    return array