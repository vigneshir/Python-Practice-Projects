import random

def choose_word(masterlist):
    word = random.choice(masterlist)
    return word

def frame_question(word):
    question=''
    tempques = random.sample(word,len(word))
    for i in range(len(tempques)):
        question+=tempques[i]
    return question    

def game():
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
       end of the game. \n\n''')
       
    masterlist = ["aberration", "abscond","abstruse","accost","adamant","admonish","adverse","advocate","affluent","ambivalent","amorphous",
                  "bland","callous","circumvent","caveat","cognizant","constituent","demagogue","didactic","equivocal","empirical","extraneous","fragrance",
                  "fortune","hegemony","homogeneous","legendary","library","literate","manoeuvre","magnanimous","munificient","nostalgia","nourishment",
                  "panacea","paradigm","plethora","renaissance","refreshment","statuette","spectacular","sporadically","ornament","ostracize","genuine",
                  "solicit","understand","unambiguity","ultrasonic","ubiquitous","voracious","whereabout" ]
    flag=0                 # flag=0 : new question to next player   flag=1 : old question to next player
    p1_attmpt, p2_attmpt = 0 , 0
    p1_corrct, p2_corrct = 0 , 0
    p1_score, p2_score = 0 , 0
    
    while(p2_attmpt<25):
        if p1_attmpt!=25:      
            if flag==0 :
                word = choose_word(masterlist)
                masterlist.remove(word)
                question = frame_question(word)
                print(question)
                repeat=0
                flag=1
            if flag==1 :
                p1answer = input("PLayer 1, your turn : ")
                p1_attmpt+=1
                flag=0
            if p1answer==word:         # if player1 gives correct answer
                p1_corrct+=1
                flag=0
                if repeat==0:
                    p1_score+=2
                    print("Player 1, your answer is correct !! You earn 2 points !\n")
                elif repeat==1:
                    p1_score+=3
                    print("PLayer 1, your answer is correct !! You earn 3 points !\n")
            elif p1answer=='0':          # player 1 wants to exit
                print("PLayer 1, you chose to end the game.")
                p1_attmpt-=1
                break
            else:                       # if player1 gives wrong answer
                if repeat==1:
                    print("PLayer 1, your answer is wrong !!\nCORRECT ANSWER : ",word,"\n")
                    flag=0
                elif repeat==0 :                  # passing question to other player
                    print("Player 1, your answer is wrong !")
                    flag=1
                    repeat=1
        else :                # if player 1 has completed 25 turns
            print("PLayer1, your turns are over.")  
        if flag==0 :               # new question for player 2
            word = choose_word(masterlist)
            masterlist.remove(word)
            question = frame_question(word)
            print(question)
            repeat=0
            flag=1
        if flag==1 : 
            p2answer=input("PLayer 2, your turn : ")
            p2_attmpt+=1
            if p2answer==word :        # player 2 gives correct answer
                p2_corrct+=1
                flag=0
                if repeat==0 :
                    p2_score+=2
                    print("PLayer 2, your answer is correct !! You earn 2 points !\n")
                elif repeat==1:
                    p2_score+=3
                    print("Player 2, your answer is correct !! You earn 3 points !\n")
            elif p2answer=='0':          # player 2 wants to quit
                print("Player 2, you chose to end the game.")
                p2_attmpt-=1
                break
            else:                      # player 2 gives wrong answer    
                if repeat==1:
                    print("Player 2, your answer is wrong !!\nCORRECT ANSWER : ",word,"\n")
                    flag=0
                elif repeat==0:
                    print("Player 2, your answer is wrong !")
                    flag=1
                    repeat=1

    
    print("\n-----------------RESULTS-----------------")
    print("                PLayer 1         Player 2")
    print("Attempts          %3d               %3d  "  % (p1_attmpt,p2_attmpt) )
    print("Correct           %3d               %3d  "  % (p1_corrct,p2_corrct) )
    print("Total Score       %3d               %3d  "  % (p1_score,p2_score) )
    
  
game()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       