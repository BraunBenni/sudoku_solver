import numpy as np
import time

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

def findNextEmpty(board, current_row, current_coloumb):
    '''
    Function to find the next empty element: rows first

    returns -1 & -1, if it can't find an empty element
    '''
    empty_row = -1 #in case sudoku is alreadey solved and we can't find an empty element
    empty_coloumb = -1 #in case sudoku is alreadey solved and we can't find an empty element
    found_empty = 0
    for i in range(current_row, 9):
        if i == current_row: #in the current row, we don't need to iterate through all columbs
            for j in range(current_coloumb, 9):
                if board[i][j] == 0:
                    empty_row = i
                    empty_coloumb = j
                    found_empty = 1 #bool to exit two for-loops
                    break
        else: #all other rows
            for j in range(0, 9):
                if board[i][j] == 0:
                    empty_row = i
                    empty_coloumb = j
                    found_empty = 1 #bool to exit two for-loops
                    break
        if found_empty: #exit loop
            break
    return empty_row, empty_coloumb


def dispend(board):
    '''
    function to dispend the board:
    '''
    for i in range(0,9):
        print(board[i])

#easy example
#board = [
#    #0 1 2 3 4 5 6 7 8
#    [0,5,9,0,0,4,7,6,0], #0
#    [0,8,0,5,7,0,3,0,0], #1
#    [0,4,3,0,0,0,0,5,0], #2
#    [1,0,0,0,4,0,6,0,0], #3
#    [0,7,0,0,6,0,0,9,0], #4
#    [0,0,2,0,8,0,0,0,7], #5
#    [0,9,0,0,0,0,1,2,0], #6
#    [0,0,7,0,2,6,0,3,0], #7
#    [0,2,6,4,0,0,9,7,0]  #8
#]

#hard example
board = [
    #0 1 2 3 4 5 6 7 8
    [0,1,0,8,0,0,7,0,0], #0
    [0,9,0,6,0,0,1,0,0], #1
    [5,0,7,0,4,0,0,6,0], #2
    [7,0,0,2,9,0,4,5,0], #3
    [0,0,0,0,0,0,0,0,0], #4
    [0,2,1,0,5,8,0,0,9], #5
    [0,7,0,0,8,0,5,0,6], #6
    [0,0,2,0,0,4,0,8,0], #7
    [0,0,6,0,0,9,0,1,0]  #8
]

start_time = time.time()

row = 0 #starting row
coloumb = 0 #starting coloumb
solved = 0
index_array = np.zeros([2,81]) #array to save edited elements (row and coloumb indices)
step = 0
while solved != 1:
    row, coloumb = findNextEmpty(board, int(row), int(coloumb)) #seraching new empty element
    print('row = ', row, '\ncoloumb = ', coloumb, '\n')
    if row == -1: #checks whether soduko is already solved (findeNextEmpty returns -1 & -1, if it can't find an empty element)
        solved = 1
        break

    number = 1
    element_passed = 0
    while element_passed != 1:
        element_passed = checkNumber(board, row, coloumb, number)
        if element_passed: #break if element passes test (and save row and coloumb indices)
            board[int(row)][int(coloumb)] = number
            index_array[0][step] = row 
            index_array[1][step] = coloumb
            step += 1
            break
        elif number in range(1,9): #element can still increase --> max: number = 8
            number += 1
        else: #reversing as many steps as necessary
            reverse = 0
            while reverse != 1:
                step -= 1
                #loading row and coloumb indices of previous step
                row = index_array[0][step] 
                coloumb = index_array[1][step]
                number = board[int(row)][int(coloumb)] #loading number of previous step
                board[int(row)][int(coloumb)] = 0 #deleting previous step --> again an empty element
                #if possible, increasing number of previous step --> otherwise keep reversing
                if number in range(1,9):
                    reverse = 1 #found step we can reverse to
                    number += 1
                   
            
end_time = time.time()

print("\n\n     --- execution time: %.7s seconds --- \n" % (end_time-start_time))

print('\n\n Solution:')
dispend(board)