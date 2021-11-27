import numpy as np

def init_board():
    '''
    11 |  12  | 13
    --------------
    21 |  22  | 23
    --------------
    31 |  32  | 33
    '''
    cell_11 = np.matrix([[1,1,1],[1,6,1],[1,1,1]])
    cell_12 = np.matrix([[2,2,2],[2,2,2],[2,2,2]])
    cell_13 = np.matrix([[3,3,3],[3,3,3],[3,3,3]])
    cell_21 = np.matrix([[4,4,4],[4,4,4],[4,4,4]])
    cell_22 = np.matrix([[5,5,5],[5,5,5],[5,5,5]])
    cell_23 = np.matrix([[6,6,6],[6,6,6],[6,6,6]])
    cell_31 = np.matrix([[7,7,7],[7,7,7],[7,7,7]])
    cell_32 = np.matrix([[8,8,8],[8,8,8],[8,8,8]])
    cell_33 = np.matrix([[9,9,9],[9,9,9],[9,9,9]])

    board = [[cell_11, cell_12, cell_13],[cell_21,cell_22, cell_23], [cell_31, cell_32, cell_33]]
    return board





def ausgabe(board):
    '''
    Textausgabe des aktuellen Boards
    '''
    print('| ', end = '') #für Anfang
    for m in range(0,3): #alle Zellenzeilen (global)
        row_global = m
        for k in range (0,3): #alle Zeilen der Zellen
            row_cells = k #Zeilen in den Zellen
            for j in range(0,3): #eine kompellte Zeile (horizontale Zellen nebeneinander)
                coloumbs_global = j
                cell = board[row_global][coloumbs_global]
                for i in range(0,3):   #eine Zeile von einer Zelle
                    coloumbs_cell = i
                    print(' ', cell.item(row_cells,coloumbs_cell), ' ',end = '') 
                print(' | ', end = '') #zwischen Zellen
    
            if row_cells == 2: #falls letzte Zeile der Zellen --> Trennlinie & Anfang neuer Zeile
                print('\n------------------------------------------------------- \n| ', end='')
            else:
                print('\n| ', end = '') #Zeilenumbruch und Anfang neuer Zeile


board = init_board()
ausgabe(board)