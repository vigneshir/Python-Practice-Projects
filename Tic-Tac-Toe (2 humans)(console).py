import numpy

def validbox(row,column):
    if row<0 or row>2 or column<0 or column>2 :
        return 0
    else:
        return 1
    
def emptybox(row,column,table):
    if table[row][column] == '-':
        return 1
    else:
        return 0
    
def printtable(table):
    for i in range(3):
        for j in range(3):
            print(table[i][j],end="   ")
        print()    
    
def win(table,row,column):
    if table[row][0]==table[row][1]==table[row][2] and table[row][0]!='-':
        return 1
    elif table[0][column]==table[1][column]==table[2][column] and table[0][column]!='-':
        return 1
    elif table[0][0]==table[1][1]==table[2][2] and table[0][0]!='-':
        return 1
    elif table[0][2]==table[1][1]==table[2][0] and table[0][2]!='-':
        return 1
    else:
        return 0
 
def tableempty(table):                 # returns 1 when table has blanks
    temp=0
    for i in range(3):
        for j in range(3):
            if table[i][j]=='-':
                temp=1
                break
    if temp==1:
        return 1
    else:
        return 0
        
def game():
    table = numpy.array([ ['-','-','-'],['-','-','-'],['-','-','-'] ])
    flag=0               # flag=1 implies 'X' or 'O' successfully inserted
    stop=0               # stop=1 implies either draw or win
    printtable(table)
    while stop==0 :
        while flag==0:
            row,column = map(int,input("X's turn : Row,Column = ").split(','))
            if validbox(row,column) :
                if emptybox(row,column,table):
                    table[row][column] = 'X'
                    printtable(table)
                    flag=1
                else:
                    print("This box is already filled ! Please choose an empty box !")
            else:
                print("Box address out of range ! Please enter correct address !")
        flag=0        
        if win(table,row,column):
            print("X won the game !!!")
            stop=1
        elif not tableempty(table):
            print("Game ended in a draw !!!")
            stop=1    
        if stop==0:
            while flag==0:
                row,column = map(int,input("O's turn : Row,Column = ").split(','))
                if validbox(row,column) :
                    if emptybox(row,column,table):
                        table[row][column] = 'O'
                        printtable(table)
                        flag=1
                    else:
                        print("This box is already filled ! Please choose an empty box !")
                else:
                    print("Box address out of range ! Please enter correct address !")
            if win(table,row,column):
                print("O won the game !!!")
                stop=1
            elif not tableempty(table):
                print("Game ended in a draw !!!")
                stop=1
            flag=0
            
game()















        
            