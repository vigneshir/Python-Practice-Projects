# def minion_game(string):                #gives memory error for large inputs
#     vowels=['A','E','I','O','U']
#     kevins_list=[]
#     stuarts_list=[]
#     for i in range(0,len(string)):
#         if string[i] in vowels :
#             for j in range(1,len(string)-i+1):
#                 kevins_list.append(string[i:i+j])
#         else:
#             for j in range(1,len(string)-i+1):
#                 stuarts_list.append(string[i:i+j])    
    
#     kevins_score= len(kevins_list)
#     stuarts_score=len(stuarts_list)
    
#     if kevins_score > stuarts_score :
#         print("Kevin",kevins_score)
#     elif kevins_score< stuarts_score:
#         print("Stuart",stuarts_score)
#     else:
#         print("Draw")        
    
# s = input()
# minion_game(s)

# def minion_game(string):                # works for any size of input
#     vowels=['A','E','I','O','U']
#     kevins_score=0
#     stuarts_score=0
#     for i in range(0,len(string)):
#         if string[i] in vowels :
#            kevins_score += len(string)-i 
#         else:
#            stuarts_score += len(string)-i   
     
#     if kevins_score > stuarts_score :
#         print("Kevin",kevins_score)
#     elif kevins_score< stuarts_score:
#         print("Stuart",stuarts_score)
#     else:
#         print("Draw")        
    
# s = input()
# minion_game(s)

# s="stringtheory"
# for character in s:
#     print(character,end="")
    
# a=['abcd\net5ecfjv','adg',3253,'\n']
# for i in a :
#     print (i)    
# print(a)

# list_A = [3,'gs','dshdj',34,654]
# set_A = set(list_A)
# set_B = {53,'dgh','dhfn',3565}
# list_B = list(set_B)
# print(set_A,list_B)

# n,m = map(int,input().split(" "))
# print(n,m)
# print(type(m))
#array =list( map(int,input().split()) )
#print(array)

# myset={'rgd','rdhf',45,7,3,'dfby658',56,8,2,8,'dhbdDHD'}
# print(myset.pop())
# print(myset)
# print(myset.pop())
# print(myset)

# set1 = { 2,3,4,5,6,7}
# set2 = { 2,3,4,5,6,7}
# print( set1.issuperset(set2) )

# print(tuple(set1))

# a,b,c,d = map( int,input().split("\n") )
# print(a,b,c,d)

# a,b,c,d = ( int( input()) for i in range(4)   )
# print(a,b,c,d)

# mylist = [3,5,56,6,23,5,96780]
# print([ mylist[i] for i in range(len(mylist)) ])
# print(mylist)
# for i in range(len(mylist)):
#     print(mylist[i],end="")
    
# print( mylist[i],end="" for i in range(len(mylist)))    

# lists = [ [3,4],[3,7],[7,3],[53,7],[7,42] ]
# print( list( lists[i] for i in range(5) ) )

# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print( int(((10**i-1)//9)**2 ))

# from collections import Counter
 
# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print ( Counter(myList) )

#req_size, price = list( map( int,input().split() ) )
#print(req_size,price)

#mytuple = (3,5,6,7,2,34)
#print( sum(mytuple) )

#print( "%.1f"% (34.64/5))

#if -5 :
#    print("true")
#else:
#    print("false")    


#intlist = [3,54,65,72,24,67,32]
# for i in intlist:
#     if str(i)[0:]==str(i)[-1:] :
#         print("true")
#     else:
#         print("false")
 
#eval("6+3")                    # doesn't return 9 when typed here, but returns when typed in console
#print( eval("6+3") )

#print( input() )

#print(print(4+7))

# mydict = { 0:3, 1:4, 2:3, 3:5}
# keylist = list( mydict.keys() )
# valuelist = list( mydict.values() )
# valuelist.sort()
# print( valuelist )
# for i in valuelist:
#     print( mydict.index(i))

        
#for i in range(2,2):
#   print("d")        

# import re
# print(bool(re.search(r'(b)?o\1','o')))
# print(bool(re.search(r'(b)?o\1','bob')))
# print(bool(re.search(r'(b)?o\1','bo')))
# print(bool(re.search(r'(b)?o\1','ob')))
# print(bool(re.search(r'(b)?o\1?','o')))


#mylist=['wre',45,57,'q',3,'sr']
#print(mylist[0:-2])

# import numpy

# table = numpy.array([ [2,4,6],[4,6,7],[7,9,8] ])
# #print(table)
# for i in range(3):
#     for j in range(3):
#         print(table[i][j],end="   ")
#     print()

#a,b = map(int,input("Enter a,b: ").split(','))
#print(a,b)
#a,b = list( map(int,input("Enter a,b: ").split(',')) )
#print(a,b)







