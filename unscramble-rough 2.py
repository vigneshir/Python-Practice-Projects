import random

def pick_word(masterlist):
    word = random.choice(masterlist)
    return word

def create_question(word):
    question = random.sample(word,len(word))
    return question

def game():
    p1attmpt=0
    p1corrct=0
    p1score=0
    p2attmpt=0
    p2corrct=0
    p2score=0
    
    while len(masterlist>0) :
        word = pick_word(masterlist)
        masterlist.remove(word)
        question = create_question(word)
        repeat = 0
        p1answer = input("PLayer1, your turn: ",question)
        if p1answer == word :
            if repeat==0:
                p1attmpt += 1
                p1corrct += 1
                p1score  += 2
            elif repeat==1 :
                p1attmpt += 1
                p1corrct += 1
                p1score  += 3
       else:
           repeat=1
           
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        