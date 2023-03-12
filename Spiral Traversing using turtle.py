# create a star using turtle
#import turtle
#tur=turtle.Turtle()
#for i in range(50):
#    tur.forward(50)
#    tur.right(144)
#turtle.done() 

# import turtle
# turtle.bgcolor("black")
# myturtle=turtle.Turtle()
# width=5
# height=7
# dot_distance=25
# turtle.setpos(-250,250)


# n = int(input("Enter length of side of square:  "))
# row,column=0,0
# k=1
# if n%2==0 :
#     k_max = n/2
# else:
#     k_max = (n+1)/2
    
# while (k<=k_max):
#     while (column<=n-k):
#         print("(%d,%d)" % (row,column), end="  ")
#         column+=1
#     column-=1    
#     while(row<n-k):
#         row+=1
#         print("(%d,%d)" % (row,column), end="  ")
#     while(column>k-1):
#         column-=1
#         print("(%d,%d)" % (row,column), end="  ")
#     while(row>k):
#         row-=1
#         print("(%d,%d)" % (row,column), end="  ")
#     column+=1  
#     k+=1


import turtle
import random

turtle.bgcolor("black")
myturtle=turtle.Turtle()
myturtle.color("white")

width=5
height=7
dot_distance=25

colorlist = ["red","blue","green","white","yellow","brown","orange","pink","violet","grey","cyan"]

myturtle.penup()
myturtle.setpos(-250,250)

n = int(input("Enter length of side of square:  "))
row,column=0,0
k=1
if n%2==0 :
    k_max = n/2
else:
    k_max = (n+1)/2
    
while (k<=k_max):
    
    chosen_color = random.randint(0,11)
    myturtle.color(colorlist[chosen_color])
    
    while (column<=n-k):
        #print("(%d,%d)" % (row,column), end="  ")
        myturtle.dot()
        myturtle.forward(dot_distance)
        column+=1
    myturtle.right(90)
    
    column-=1    
    while(row<n-k):
        row+=1
        #print("(%d,%d)" % (row,column), end="  ")
        myturtle.dot()
        myturtle.forward(dot_distance)
    myturtle.right(90)
    
    while(column>k-1):
        column-=1
        #print("(%d,%d)" % (row,column), end="  ")
        myturtle.dot()
        myturtle.forward(dot_distance)
    myturtle.right(90)
    
    while(row>k):
        row-=1
        #print("(%d,%d)" % (row,column), end="  ")
        myturtle.dot()
        myturtle.forward(dot_distance)
    myturtle.right(90)
    
    column+=1  
    k+=1   
   
turtle.done()