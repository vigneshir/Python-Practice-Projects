# player swaps door.  played for 500 times
# doors : index of list door_contents
# goat : G   car : C

import random

win=0

for i in range(500):
    door_contents=['G','G','G']
    car_door = random.choice([0,1,2])
    door_contents[car_door]='C'
    
    chosen_door = random.choice([0,1,2])
    
    temp=[0,1,2]
    temp.remove(chosen_door)
    
    if chosen_door==car_door:                      # both remaining doors contain goats
        exposed_door = random.choice(temp)
        temp.remove(exposed_door)
        final_choice = temp[0]
    else:                                          # remaining doors contain goat and car    
        temp.remove(car_door)
        exposed_door = temp[0]
        final_choice = car_door
        
    print(" Initially Chosen Door: ",chosen_door)
    print("          Exposed Door: ",exposed_door)
    print("   Finally Chosen Door: ",final_choice)
    print("   Door containing car: ",car_door,"\n")
    
    if door_contents[final_choice]=='C':
        win += 1 
        
print("Wins out of 500 : ",win)
print("Winning percent : ",win/5)        


