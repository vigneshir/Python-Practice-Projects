def find_n(name1, name2):
    for i in range(len(name1)):
        for j in range(len(name2)):
            if name1[i]==name2[j]:
                name1[i]=""
                name2[j]=""
                break
    temp = name1+name2
    n=0
    for ch in temp:
        if ch!="":
            n+=1
    return n

def find_relation(n):
    word=list("FLAMES")
    print(word)
    while len(word)!=1 :
        word_size = len(word)
        temp_n = n
        while temp_n > word_size :
            temp_n -= word_size
        if temp_n == 1 :
            word = word[1:]
            print(word)
        elif temp_n == 0 :
            word = word[0:word_size-1]
            print(word)
        else:
            word = word[temp_n:] + word[:temp_n-1]
            print(word)
      
    result_decoder = { 'F':'Friends', 'l':'Lovers', 'A':'Affection','M':'Married','E':'Enemies','S':'Sibling'}    
    
    return result_decoder[word[0]]

def driver_function():
    name1 = list( input("Name of the boy: ") )
    name2 = list( input("Name of the girl: ") )
    n = find_n(name1,name2)
    print(n)
    print("Relation between them: "+ find_relation(n) )
    
driver_function()    
        