# two player game
# each player will get 4 chances to guess letters in car name and 3 to guess the car name 
# an option will be provided to give up and tell computer to display answer
# an option will be provided to end the game in between, after which the score of each player till then will be displayed



import random

print("Please enter your name: ")
player1 = input("Player 1 : ")
player2 = input("Player 2 : ")

masterlist = [ "MARUTI SUZUKI","SUZUKI","MAHINDRA","TATA","HONDA","MERCEDES BENZ","JAGUAR","lAMBORGHINI","BENTLEY","PORSCHE","BMW","AUDI","FERRARI","MINI","MCLAREN","FORD","VOLKSWAGEN","ASTON MARTIN" ]

turn=1   
score1 = 0
score2 = 0
anschance1 = 3
anschance2 = 3
guesschance1 = 4
guesschance2 = 4

def choose():
   questpos = random.randint(0,len(masterlist))
   quest = masterlist[questpos]
   return quest
   
def checkanswer(inpanswer):
    # inpanswer = input("Enter your answer: ")
    # while(inpanswer != response):
    #     print("Incorrect answer. You have",anschance1,"chance(s) to answer and", guesschance1,"chance(s) to guess a letter.")    
    # if (inpanswer == choose()):
    #     print("Congratulations, it is the right answer !")
    #     print("Scoreboard : ", player1,":", score1, "  ", player2,":", score2)
    if (inpanswer == choose()):
        return 1
    else:
        return 0
 
def guess(inpguess):
    for j in range(0,len())
        chooose()
    
        

if (turn%2 != 0):
    print( player1,", it's your turn to guess the name of the car company: ")    
    for i in range(0, len(choose())):
        if (choose()[i] != " "):    
            print("_", end=" ")    
        else:
            print(" ", end=" ")            
    
    response = input("Enter a response ('a' to answer, 'b' to guess a letter, 'c' to end the game): ")    
    
    if (response == "a"):
        anschance1 -= 1
        inpanswer = input("Enter your answer: ")
        if (checkanswer(inpanswer) == 1):
            print("Correct Answer !")
            print("Scoreboard :  ", player1,":", score1, "  ", player2,":", score2)
        else :
            anschance1 -= 1
            print("Wrong Answer ! Chances left:  Answering: ", anschance1, "Guessing a letter: ", guesschance1)
    
    elif (response == "b"):
        inpguess = input("Enter your guess of a letter present in the answer: ")
        guess(inpguess)
    elif (response == "c"):
        endgame()
    else:
        print("Please enter a valid response.")
          

   

