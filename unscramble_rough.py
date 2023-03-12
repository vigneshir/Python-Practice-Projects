print("...............Unscramble..................")
print('''Welcome to this two-player game which tests your familiarity with the spellings of English words...

Rules:
1. Every correctly unscrambled word has 2 points.
2. If a player gives an incorrect answer, the same question is forwarded to the other player.
   If the other player manages to give the correct answer, then 1 additional point is awarded to him/her
   along with the 2 points for the correct answer.
3. The correct answer would be displayed if neither player gives the correct answer.   
4. The game will end when each player attempts 25 different questions. You can also end the game before this by 
   entering '0' as the answer for the current question. 
5. The final result - number of questions attempted and correctly answered by each plaer will be displayed at the 
   end of the game.  
 
Press 'Enter' to start the game.  ''')

def game():
    print("Please enter your name: ")
    p1 = input("Player 1 : ")
    p2 = input("Player 2 : ")
    
    pp1 = 0
    pp2 = 0
    turn = 0
    
    exhausted1 = []
    exhausted2 = []
    
    picked_word1 = pick1() 
    exhausted1.append( picked_word1 )
    
    picked_word2 = pick2()
    exhausted2.append( picked_word2 )
    
    if( turn%2 == 0 ):
        if( set(exhausted1) != set(list1) ):
            print("To player ", p1, " :    ", scramble( picked_word1 ) )
            response = input()
            if( response == picked_word1 ):
                print("Your answer is correct.")
                pp1 = pp1+2
                turn = turn + 1
                print("Total Points:  ", p1, " : ", pp1,"    ", p2, " : ", pp2)
            elif( response == 0 ):
                print("The game has ended.")
                print("Total Points-  ", p1, " : ", pp1,"    ", p2, " : ", pp2)
                if( pp1 > pp2 ):
                    print("Player ", p1, " won the game.")
                elif( pp1 < pp2 ):
                    print("Player ", p2, " won the game.")
                else :
                    print("The game has ended in a draw.")
                break
    
             else:
                print("Your answer is incorrect.")
                turn = turn+1
                print("Total Points:  ", p1, " : ", pp1,"    ", p2, " : ", pp2)
                
                
            
            
    
    
    
    
    
       
if( input() == "\n" ):
    game()
    
    
