import random
import numpy as np

def checkNumber(board, row, coloumb, number):
    '''
    Function checks whether new number is valid:
    '''
    passed = 1

    #check row:
    for i in range(0,8):
        if board[int(row)][i] == number:
            passed = 0

    #check coloumb:
    for i in range(0,8):
        if board[i][int(coloumb)] == number:
            passed = 0
    
    #check cell:
    if row in range(0,3): #first row of cells
        row_cell = 0
    elif row in range(3,6): #second row of cells
        row_cell = 1
    elif row in range(6,9): #third row of cells
        row_cell = 2

    if coloumb in range(0,3): #first coloumb of cells
        coloumb_cell = 0
    elif coloumb in range(3,6): #second coloumb of cells
        coloumb_cell = 1
    elif coloumb in range(6,9): #third coloumb of cells
        coloumb_cell = 2
    for i in range(0+3*row_cell, 3+3*row_cell): #rows of cell, number is in
        for j in range(0+3*coloumb_cell, 3+3*coloumb_cell): #coloumbs of cell, number is in
            if board[i][j] == number:
                passed = 0

    return passed

def dispend(board):
    '''
    function to dispend the board:
    '''
    for i in range(0,9):
        print(board[i])


def generate_sudoku(empty_elements):
    board = np.zeros([9,9])

    iter  = 0
    while iter < empty_elements:
        iter  = iter + 1

        #search random position
        row = random.randrange(0,9)
        coloumb = random.randrange(0,9)

        #generate valid number
        number = random.randrange(0,9)
        passed = 0
        while passed != 1:
            number = random.randrange(0,9)
            passed = checkNumber(board, row, coloumb, number)
        board[row][coloumb] = number

    return board



