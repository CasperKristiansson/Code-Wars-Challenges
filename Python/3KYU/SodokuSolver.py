"""
Write a function that will solve a 9x9 Sudoku puzzle.
The function will take one argument consisting of the
2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy"
(i.e. determinable; there will be no need to assume and
test possibilities on unknowns) and can be solved with a
brute-force approach.

puzzle = [[5,3,0,0,7,0,0,0,0],
		  [6,0,0,1,9,5,0,0,0],
		  [0,9,8,0,0,0,0,6,0],
		  [8,0,0,0,6,0,0,0,3],
		  [4,0,0,8,0,3,0,0,1],
		  [7,0,0,0,2,0,0,0,6],
		  [0,6,0,0,0,0,2,8,0],
		  [0,0,0,4,1,9,0,0,5],
		  [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
"""


# def find_empty(puzzle):
# 	for x, row in enumerate(puzzle):
# 		for y, col in enumerate(row):
# 			if col == 0:
# 				return {x, y}

# 	return False


# def is_valid(puzzle, x, y, i):
# 	for row in puzzle:
# 		if row[y] == i:
# 			return False

# 	for col in puzzle[x]:
# 		if col == i:
# 			return False

# 	x_start = (x // 3) * 3
# 	y_start = (y // 3) * 3
# 	for x in range(x_start, x_start + 3):
# 		for y in range(y_start, y_start + 3):
# 			if puzzle[x][y] == i:
# 				return False


# def clear_map(puzzle, marked, x, y):
# 	for i in range(1,10):
# 		if marked[y][i]:
# 			puzzle[x][y] = 0

# 	for i in range(1,10):
# 		if marked[i][y]:
# 			puzzle[x][y] = 0
	
# 	x_start = (x // 3) * 3
# 	y_start = (y // 3) * 3
# 	for x in range(x_start, x_start + 3):
# 		for y in range(y_start, y_start + 3):
# 			if marked[x][y]:
# 				puzzle[x][y] = 0

# 	return puzzle


# def find_number(puzzle, marked, x, y):
# 	for i in range(1, 10):
# 		if is_valid(puzzle, x, y, i):
# 			puzzle[x][y] = i
# 			return True
	
# 	puzzle = clear_map(puzzle, marked, x, y)
# 	find_number(puzzle, marked, x, y)


# def solve(puzzle, marked):
# 	empty = find_empty(puzzle)
# 	if empty is not False:
# 		x, y = empty
# 		puzzle = find_empty(puzzle, marked, x, y)


# def sudoku(puzzle):
# 	marked = [[0 for x in range(10)] for y in range(10)]
# 	for x, row in enumerate(puzzle):
# 		for y, col in enumerate(row):
# 			if col == 0:
# 				marked[x][y] = 1
	
# 	solve(puzzle, marked)

# 	return puzzle
M = 9

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

print(Suduko(puzzle, 0, 0))
print(Suduko(puzzle, 0, 0) == solution)