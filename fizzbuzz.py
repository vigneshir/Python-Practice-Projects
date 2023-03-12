print(".....Fizzbuzz.....")
n = print("What should the last number of the game be : ")
n = int(input())
i = 1
while (i <= n) :
    if( (i%3 == 0) and (i%5 != 0) ) :
        print("Fizz")
        i = i+1
    
    elif( (i%3 != 0) and (i%5 == 0) ) :
        print("Buzz")
        i = i+1
        
    elif( (i%3 == 0) and (i%5 == 0)) :
        print("Fizzbuzz")
        i = i+1
    else :
        print(i)
        i = i+1
