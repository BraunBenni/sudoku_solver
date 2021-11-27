import numpy as np
import time


def init_board(manual_input):

    '''
    11 |  12  | 13
    --------------
    21 |  22  | 23
    --------------
    31 |  32  | 33
    '''

    if manual_input:
        #initialisieren
        cell_11 = np.ones((3,3)) * -1
        cell_12 = np.ones((3,3)) * -1
        cell_13 = np.ones((3,3)) * -1
        cell_21 = np.ones((3,3)) * -1
        cell_22 = np.ones((3,3)) * -1
        cell_23 = np.ones((3,3)) * -1
        cell_31 = np.ones((3,3)) * -1
        cell_32 = np.ones((3,3)) * -1
        cell_33 = np.ones((3,3)) * -1
        board = [[cell_11, cell_12, cell_13],[cell_21,cell_22, cell_23], [cell_31, cell_32, cell_33]]
        board_names = [['cell_11', 'cell_12', 'cell_13'],['cell_21','cell_22', 'cell_23'], ['cell_31', 'cell_32', 'cell_33']]


        print('----------------------------------')
        print('Manuelle Eingabe von Zahlen: \n')
        for i in range(0,3): #globale Zeilen des Boards
            row_global = i
            for j in range(0,3): #globale Spalten des Boards
                coloumb_global = j
                cell = board[row_global][coloumb_global]
                cell_name = board_names[row_global][coloumb_global]
                print('Eingabe von Zelle ', cell_name,':')
                for k in range(0,3): #Zeilen der Zelle
                    row_cell = k
                    for l in range(0,3): #Spalten der Zelle
                        coloumb_cell = l
                        print('Zeile:', row_cell+1, ' Spalte:', coloumb_cell+1, ' ', end='')
                        temp = input()
                        cell[row_cell][coloumb_cell] = int(temp) 

    else:   #vorgefertigter Input
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
    
    time.sleep(1)
    return board


def test_board(board):
    '''
    Ueberpruefen der Eingabe:
        ausgefuellte Felder: 0 - 9
        leere Felder: -1
    '''

    passed = 1
    for i in range(0,3): #globale Zeilen des Boards
            row_global = i
            for j in range(0,3): #globale Spalten des Boards
                coloumb_global = j
                cell = board[row_global][coloumb_global]
                for k in range(0,3): #Zeilen der Zelle
                    row_cell = k
                    for l in range(0,3): #Spalten der Zelle
                        coloumb_cell = l
                        element = cell.item(row_cell, coloumb_cell)
                        if element not in range (-1,10):
                            passed = 0
    #Ausgabe
    if passed == 0:
        print("\n\n [WARNUNG:] Fehlerhafte Eingabe!! Nur Werte zwischen 0 und 9 & -1 fuer leeres Fekd moeglich")
    else:
        print("\n\n Eingabetest bestanden!")




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
            
            if row_global == 2 and row_cells == 2: #falls gloabl letzte Zeile der Zellen --> Trennlinie & KEIN Anfang neuer Zeile
                print('\n-------------------------------------------------------')
            elif row_cells == 2: #falls letzte Zeile der Zellen --> Trennlinie & Anfang neuer Zeile
                print('\n------------------------------------------------------- \n| ', end='')
            else:
                print('\n| ', end = '') #Zeilenumbruch und Anfang neuer Zeile


manual_input = 0
board = init_board(manual_input)
ausgabe(board)
test_board(board)


time.sleep(3)
