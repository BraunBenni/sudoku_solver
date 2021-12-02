def checkNumber(board, row, coloumb, number):
    '''
    Function checks whether new number is valid:
    '''
    passed = 1

    #check row:
    for i in range(0,8):
        if board[row][i] == number:
            passed = 0

    #check coloumb:
    for i in range(0,8):
        if board[i][coloumb] == number:
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

def findNextEmpty(board, current_row, current_coloumb):
    '''
    Function to find the next empty element: rows first
    '''
    found_empty = 0
    for i in range(current_row, 9):
        if i == current_row: #in the current row, we don't need to iterate through all columbs
            for j in range(current_coloumb, 9):
                if board[i][j] == 0:
                    empty_row = i
                    empty_coloumb = j
                    found_empty = 1 #bool to exit two for-loops
                    break
        else:
            for j in range(0, 9):
                if board[i][j] == 0:
                    empty_row = i
                    empty_coloumb = j
                    found_empty = 1 #bool to exit two for-loops
                    break
        if found_empty: #exit loop
            break
    return empty_row, empty_coloumb



board = [
    [7,8,0,4,0,0,1,2,0], #0
    [6,0,0,0,7,5,0,0,9], #1
    [0,0,0,6,0,1,0,7,8], #2
    [0,0,7,0,4,0,2,6,0], #3
    [0,0,1,0,5,0,9,3,0], #4
    [9,0,4,0,6,0,0,0,5], #5
    [0,7,0,3,0,0,0,1,2], #6
    [1,2,0,0,0,7,4,0,0], #7
    [0,4,9,2,0,6,0,0,7]  #8
]

