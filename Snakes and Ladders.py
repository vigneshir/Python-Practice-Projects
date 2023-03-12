# based on snakes and ladders board downloaded as word document in same directory
# extra chance on getting 6 
# no extra chance for climbing ladder

import random

def roll_dice():
    return random.choice([1,2,3,4,5,6])

def snakes_ladders(playerpos):
    snakeladder= { 3:20, 6:14, 11:28, 15:34, 17:74, 22:37, 38:59, 49:67, 57:76, 61:78, 73:86, 81:98, 88:91,
                  8:4, 18:1, 26:10, 39:5, 51:14, 54:36, 56:1, 60:23, 75:28, 83:45, 85:59, 90:48, 92:25, 97:87, 99:63 }
    if playerpos in snakeladder:
        return snakeladder[playerpos]
    else:
        return playerpos
    
def game():
    p1pos, p2pos = 1,1
    print("-----------SNAKES AND LADDERS-------------")
    print("PLayer 1 initial position : %d\nPlayer 2 initial position : %d\n" % (p1pos,p2pos))
    dice=0
    flag=0        # flag=1 implies exit from game
    six=0         # dummy for repeating turn on getting six
    while (p1pos!=100 and p2pos!=100 and flag==0) :
        while six==0:
            six=1
            flag = int( input("Player 1, your turn. Enter 0 to roll the dice or 1 to end the game : ") )
            if flag==0:
                dice = roll_dice()
                print("Dice value : ",dice)
                if ( 100-dice >= p1pos ):               # possible movements of pawn
                    p1pos+=dice
                    print("Player 1 position: ",p1pos)
                    modf_p1pos = snakes_ladders(p1pos)
                    if modf_p1pos > p1pos :
                        print("Player 1, you encountered a ladder ! Player 1 final position : ",modf_p1pos,"\n")
                        p1pos=modf_p1pos
                    elif modf_p1pos < p1pos :
                        print("Player 1, you encountered a snake !  Player 1 final position : ",modf_p1pos,"\n")
                        p1pos=modf_p1pos
                    else:
                        print()
                    if p1pos==100 :
                        print("Player 1 won the game !!!")
                    if dice==6 :
                        six=0
                        print("Player 1 got a 6 on the dice ! Hence an extra turn !")
                else:
                    print()
                    if dice==6:
                        six=0
                        print("Player 1 got a 6 on the dice ! Hence an extra turn !")
            else :
                print("Player 1 chose to end the game !")
        six=0       
        if (p1pos!=100 and flag==0):
            while six==0:
                six=1
                flag = int( input("Player 2, your turn. Enter 0 to roll the dice or 1 to end the game : ") )
                if flag==0:
                    dice = roll_dice()
                    print("Dice value : ",dice)
                    if ( 100-dice >= p2pos ):               # possible movements of pawn
                        p2pos+=dice
                        print("Player 2 position: ",p2pos)
                        modf_p2pos = snakes_ladders(p2pos)
                        if modf_p2pos > p2pos :
                            print("Player 2, you encountered a ladder ! Player 2 final position : ",modf_p2pos,"\n")
                            p2pos=modf_p2pos
                        elif modf_p2pos < p2pos :
                            print("Player 2, you encountered a snake !  Player 2 final position : ",modf_p2pos,"\n")
                            p2pos=modf_p2pos
                        else:
                            print()
                        if p2pos==100 :
                            print("Player 2 won the game !!!")
                        if dice==6 :
                            six=0
                            print("Player 2 got a 6 on the dice ! Hence an extra turn !")
                    else:
                        print()
                        if dice==6:
                            six=0
                            print("Player 2 got a 6 on the dice ! Hence an extra turn !")
            
                else :
                    print("Player 2 chose to end the game !")
            six=0    
                
game()                    
                        
            
    
    
    
    