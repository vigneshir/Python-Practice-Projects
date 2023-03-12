# one player game
# first print coded word. Ask for letter to be unlocked. if entered letter exists, unlock i and print. else go down.
# ask user "0 to guess letter, 1 to guess word"
# if 0, do as above.
# if 1, accept input word. if correct: won,flag=1 if not correct, go above.
 
import random

masterlist = [ "MARUTI SUZUKI","SUZUKI","MAHINDRA","TATA","HONDA","MERCEDES BENZ","JAGUAR","lAMBORGHINI","BENTLEY","PORSCHE","BMW","AUDI","FERRARI","MINI","MCLAREN","FORD","VOLKSWAGEN","ASTON MARTIN" ]

question = random.choice(masterlist)

codedques=""
temp=list(question)
for i in range(len(temp)):
    if (temp[i]!=" "):
        temp[i]="*"
    else:
        temp[i]=" "
codedques = "".join(temp)

print(codedques)
guessletter = input("Guess a letter in the car name: ")
modcodedques = list(codedques)
if guessletter in question:
    for i in range(len(question)):
        if (guessletter==question[i]):
            modcodedques[i] = guessletter 
    for i in range(len(question)):
        print(modcodedques[i],end="")
        
else:
    print("This letter is absent in the car name")
        