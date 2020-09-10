# Not a definitive solution to create a sudoku puzzle. This is not OK.

from random import randrange

sudoku_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

GRID_SIZE = len(sudoku_grid)
maxnumber_of_tips = 17  # Some tests on algorithms on internet show that something around 17 is the number of tips generated with this algorithm that produce a puzzle with solution

def verify_subgrid(number, row, col):
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if sudoku_grid[i][j] == number:
                    return False
    return True


def verify_col(number, col):
    for i in range(0,9):
        if number == sudoku_grid[i][col]:
            return False
    return True


def create_sudoku(sudoku_grid, maxnumber_of_tips):
    counter = 0
    while counter < maxnumber_of_tips:
        row = randrange(0,9)
        col = randrange(0,9)
        number = randrange(1,10)
        if sudoku_grid[row][col] == 0: # Verify if the cell is empty
            if not number in sudoku_grid[row]: # Verifiy if there is not the number at the row
                if verify_col(number,col):  # Verifiy if there is not the number at the column
                    if verify_subgrid(number, row, col):# Verifiy if there is not the number at the subgrid
                        sudoku_grid[row][col]=number
                        counter += 1
                        #print(counter)
    return True

create_sudoku(sudoku_grid, maxnumber_of_tips)
for cell in sudoku_grid:
    print(cell)

#print(sudoku_grid)