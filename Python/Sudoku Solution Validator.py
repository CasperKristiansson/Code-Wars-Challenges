# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python

def valid_solution(board):       
    for row_index, row in enumerate(board):
        for number_index, number in enumerate(row):
            if number == 0: return False

            for i in range(9):
                if number == board[row_index][i] and i != number_index: return False

            for i in range(9):
                if number == board[i][number_index] and i != row_index: return False
            
            if(number_index < 3):
                init_x = 0
            elif(number_index < 6):
                init_x = 3
            else:
                init_x = 6

            if(row_index < 3):
                y = 0
            elif(row_index < 6):
                y = 3
            else:
                y = 6

            for _ in range(3):
                x = init_x
                for _ in range(3):
                    if number == board[y][x] and (row_index != y and number_index != x): return False
                    x += 1
                y += 1

    return True
