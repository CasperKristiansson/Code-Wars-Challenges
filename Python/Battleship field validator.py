# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

def validate_battlefield(field):
    marked = [[0 for x in range(10)] for y in range(10)]
    cell_4 = cell_3 = cell_2 = cell_1 = 0
    
    for y, row in enumerate(field):
        for x, position in enumerate(row):
            
            if position == 1 and not marked[y][x]:
                c_x, c_y = x, y
                
                while True:
                    if c_x != 9 and field[y][c_x + 1]:
                        if c_x != 0 and y != 9 and field[y + 1][c_x - 1]:
                            return False
                        elif(y != 9 and field[y + 1][c_x + 1]):
                            return False
                        c_x += 1
                        marked[y][c_x] = 1
                    else:
                        if c_x != 0 and y != 9 and field[y + 1][c_x - 1]:
                            return False
                        elif(y != 9 and c_x != 9 and field[y + 1][c_x + 1]):
                            return False
                        break
                        
                if c_x != x:
                    if c_x - x + 1 == 4:
                        cell_4 += 1
                    elif c_x - x + 1 == 3:
                        cell_3 += 1
                    elif c_x - x + 1 == 2:
                        cell_2 += 1
                    else:
                        return False
                
                else:
                    while True:
                        if c_y != 9 and field[c_y + 1][x]:
                            if c_x != 0 and field[y + 1][c_x - 1]:
                                return False
                            elif(c_x != 9 and field[y + 1][c_x + 1]):
                                return False
                            c_y += 1
                            marked[c_y][x] = 1
                        else:
                            if c_x != 0 and c_y != 9 and field[y + 1][c_x - 1]:
                                return False
                            elif(c_x != 9 and c_y != 9 and field[y + 1][c_x + 1]):
                                return False
                            break
                    if c_y != y:
                        if c_y - y + 1 == 4:
                            cell_4 += 1
                        elif c_y - y + 1 == 3:
                            cell_3 += 1
                        elif c_y - y + 1 == 2:
                            cell_2 += 1
                        else:
                            return False                        
                        
                if(x == c_x and y == c_y):
                    cell_1 += 1

            marked[y][x] = 1

    return (cell_4 == 1 and cell_3 == 2 and cell_2 == 3 and cell_1 == 4)
    