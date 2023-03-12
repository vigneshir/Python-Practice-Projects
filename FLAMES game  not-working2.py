# wring logic, doesn't take into account star index of counting

def find_count(name1, name2):
    name1 = list(name1)
    name2 = list(name2)
    i,j=0,0
    while i < len(name1) :
        while j < len(name2) :
            if name1[i] == name2[j]:
                name2.remove(name2[j])
                j-=1
                name1.remove(name1[i])
                i-=1
            j+=1
        i+=1    
    return len(name1)+len(name2)

def find_relation(name1,name2,count):
    word = list("FLAMES")
    cutletterpos = count
    iterations=1      
    while iterations<=5 :
        if cutletterpos>len(word):
            cutletterpos=cutletterpos-len(word)                 # valid for all iterations even in startindex !=0 because word is modified in that way after each iteration
        word[cutletterpos-1]=0
        newword = []
        for letter in word:
            if letter!=0:
                newword.append(letter)
        word = newword[:]
        iterations+=1    
    return word[0]

def game():
    name1 = input("Player 1, enter your name: ")
    name2 = input("Player 2, enter your name: ")
    count = find_count(name1,name2)
    print("Count: ",count)
    print("The relation between you both is ",find_relation(name1,name2,count))
    
  
game()     