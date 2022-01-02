# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    if(len(walk) != 10):
        return False
    x = y = 0
    for direction in walk:
        if direction == 'e':
            y += 1
        elif direction == 'n':
            x += 1
        elif direction == 's':
            x -= 1
        elif direction == 'w':
            y -= 1

    return (x == 0 and y == 0)
