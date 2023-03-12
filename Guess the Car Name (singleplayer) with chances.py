import random

def create_question():
    masterlist = [ "MARUTI SUZUKI","SUZUKI","MAHINDRA","TATA","HONDA","MERCEDES BENZ","JAGUAR","lAMBORGHINI","BENTLEY","PORSCHE","BMW","AUDI","FERRARI","MINI","MCLAREN","FORD","VOLKSWAGEN","ASTON MARTIN","MITSUBHISHI" ]
    question = random.choice(masterlist)
    return question

def unlockchr(inpchr, modf_ques, question):         # returns 1 if match not found, else returns unlocked question
    if inpchr in question :
        modf_modf_ques=''
        for i in range(len(question)):
            if question[i]!=inpchr :
                modf_modf_ques += modf_ques[i]
            else:
                modf_modf_ques += inpchr 
        return modf_modf_ques        
    else :
        return 1
    

# creating the coded question and printing it 
def create_codedquestion(question):
    modf_ques = ''
    for i in range(len(question)) :
        if question[i]!=' ':
            modf_ques += '*'
        else:
            modf_ques+=' '
    return modf_ques


def game():
    
    print("GUESS THE CAR NAME : 4 CHANCES FOR GUESSING LETTERS (except when no letter has been decoded), 2 FOR GUESSING ANSWER (USE CAPITAL LETTERS THROUGHOUT)")
    question = create_question()
    modf_ques = create_codedquestion(question)
    print(modf_ques)
    
    inpchr = input("Enter a character to unlock in the question: ")
    temp = unlockchr(inpchr, modf_ques, question)
    
    while temp==1 :                       # i.e question has no decoded chrs 
        print("Letter not found in car name!")
        inpchr = input("Enter a character to unlock in the question: ")
        temp = unlockchr(inpchr, modf_ques, question)
    
    #now temp contains first time decoded question 
    print(temp)
    print()
    answerexposed=0
    letter_chances=4
    answer_chances=2
    
    while (answerexposed == 0 and letter_chances>=0 and answer_chances>0):
        
        response = int(input("Enter 1 to guess another letter or 2 to guess the car name: "))
        if response==1 :
            if (letter_chances==0 and answer_chances>0):
                print("Sorry, chances for guessing a letter are over.")
            else:
                letter_chances-=1
                inpchr = input("Enter a character to unlock in the question: ")
                temp2 = unlockchr(inpchr, temp, question)
                if temp2==1 :
                    print("Letter not found in car name!")
                    # temp remains unchanged
                else :
                    print(temp2)
                    temp=temp2[:]
                    if temp==question :
                        answerexposed=1
                        print("You unlocked the car name but did not guess it on your own !!!\nGAME HAS ENDED.")
       
        elif response==2 :
            answer_chances-=1
            guessname = input("Enter your answer: ")
            if guessname==question :
                print("Congratulations, you correctly guessed the car name !!!\nGAME HAS ENDED.")
                answerexposed=1
            else:
                print("Incorrect answer !!!")
        
        print("")
        
    if (answerexposed==0 and answer_chances==0):
        print("Your chances for answering are over.\nThe correct answer is",question)
        print("GAME HAS ENDED.")
            
        
        
game()        
            
            
        
        
    

   
    
   

   
    
   
    
   
    
   
    
    
    


