# player does not swap door.  played for 500 times
# doors : index of list door_contents
# goat : G   car : C

import random

win=0

for i in range(500):
    door_contents=['G','G','G']
    car_door = random.choice([0,1,2])
    door_contents[car_door]='C'
    chosen_door = random.choice([0,1,2])
    print("        Chosen Door: ",chosen_door)
    print("Door containing car: ",car_door,"\n")
    if door_contents[chosen_door]=='C':
        win += 1 
        
print("Wins out of 500 : ",win)
print("Winning percent : ",win/5)        


