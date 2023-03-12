# accepting input from user (note no 'print' inside input())
# n = input("Enter the number: ")
# print(n)

#accepting multiple inputs from user
#method 1 : using split()
# a,b,c = input("Enter three numbers separated by space: ").split()
# print(a,b,c)
# print( type(a) )
# a,b,c,d,e = input("Enter five numbers separated by commas: ").split(",")
# print(a,b,c,d,e)

# print("The 5 words are: ",input("Enter 6 or more words separated by space: ").split(" ",5))

# typecasting to int
# x = list(map(int, input("Enter multiple values: ").split()))
# print("List of entered values: ", x)

# method 2 : using list definintion
# x, y, z = [int(x) for x in input("Enter three values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print("Third Number is: ", z)
# print()

# formatted output (numbers)
# print("%5.2f" % 5.33333)
# print(005.3333)
# print("%18.4f"% 23.4)

# formatted output (string)
# print("{} trains are very {}".format("Local","crowded."))
# print("{1} trains are very {0}".format("crowded.","Local"))
# print("{typeoftrain} trains are very {occupancy}".format( typeoftrain = "Local", occupancy = "crowded."))
# print("Cost Price is {1:.2f} and Selling Price is {0:.2f}".format(5063.24,7342.56))
# print("Cost Price is {cp:.2f} and Selling Price is {sp:.2f}".format( sp=5063.24, cp=7342.56))
# print("{0:<8} is where {1:^5} am studying {2:>25}".format("KJSCE","I","computer engineering"))


# string operations
# origstring = "Apple is a red-coloured fruit."

# origlist = list(origstring)
# # print(origlist)

# # print(origstring[-1])
# # print(origstring[3:27:2])
# #print(origstring[::-1])

# # origstring[3] = 'a'
# # print(origstring)

# # method 1 to change contents of a string indirectly - by creating another string with modified entries
# origlist[4] = 'a'
# origlist[11:14] = 'black'
# modlist1 = origlist
# modstring1 = "".join(modlist1)  # note how to create a string with a list
# print(modstring1)


# # method 2
# modstring2 = origstring[0:4] + 'a' + origstring[5:11] + 'black' + origstring[14:30]

# # note : though string elements cannot be modified, the entire string can be modified
# origstring = "Banana is a yellow-coloured fruit"
# print(origstring)



# array = [[0 for j in range(3)] for i in range(3)]

# t=1
# for i in range(3):
#     for j in range(3):
#         array[i][j] = t
#         t = t+1

# for i in range(3):
#     for j in range(3):
#         print(array[i][j] , end = "  ")
#     print("") 


#import string
#print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# str = "abcdefg"
# strlist = list(str)
# print (strlist)



# a,b,c = input().split()
# print (a,b,c)

# list = [3,5,63,"fsg","shj",6]
# print(tuple(list))




# print(int('a'))
# print(ord('a'))
# print( chr(ord('a')))

# mylist = [2,34,'gd','hdz',46]
# mystring = str(mylist)
# print(mystring)
# print("-".join(mylist))
# print("-".join(mystring))
# map(str,mylist)
# print("-".join(mylist))
#print(mylist[-4:-1])

# s='hbfgn'
# s[0].upper()
# print(s)

# list = ['ad','grh','hrg','hn','34fa']
# print(list[1][2])
# word = list[0].upper()+list[1]
# print(word)
# list.append(word)
# print(list)

# def solve(s):                  # runtime error if multiple consecutive spaces
#     name=""
#     words = s.split(" ")
#     print (words)
#     for word in words:
#           word = word[0].upper()+ word[1:]
#           name = name + word + " "
#     return name      

# s = input()
# print(solve(s))

# def solve(s):                         # works for consecutive spaces as well
#     if s[0]!=" ":
#         print(s[0].upper(),end="")
#     else:
#         print(s[0],end="")        
#     for i in range(1,len(s)):
#         if s[i]!=" ":
#             if s[i-1]==" " :
#                print(s[i].upper(),end="")
#             else:
#                 print(s[i],end="")    
#         else:
#             print(" ",end="")

# s=input()
# solve(s)


# list=[]
# string="Engineering"
# list.append(string[3:11])
# print(list)


# string = '454+45j'
# print(list(string))
# print(str(list(string)))

# import math
# print( math.ceil(4.4))
# print( round(4.5))
# print( chr(176))

#print( 34 == 34.00000)

#mylist= ['sgb','\n','etg','rgdfvhn','fbxb','\n', 'eyhr','\n','jkvhj','\n','sgsf','\n','sdfb']
# print(mylist)
# print(str(mylist))
#print("".join(mylist))
# mylist.insert(2,'rdgb')
# print(mylist)

# k = '6'
# k =int(k)
# print(k)















