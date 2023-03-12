import string
import random

print("Spot the similar character...")

masterlist = list(string.ascii_letters)

list1 = random.sample(masterlist,5)

samechrposin1 = random.randint(0,4)
samechr = list1[samechrposin1]

samechrposin2 = random.randint(0,4)

list2 = []

for chosenchr in list1:
    for masterchr in masterlist:
        if (chosenchr == masterchr):
            masterlist.remove(masterchr)
            
list2 = random.sample(masterlist,4)
list2.insert(samechrposin2,samechr)

print("List 1:  ", end="")
for i in range(0,5):
    print(list1[i], end="  ")
print("")

print("List 2:  ", end="")
for i in range(0,5):
    print(list2[i], end="  ")
print("")
    
response = input("Character common in both lists : ")
if (response == samechr):
    print("Correct!!! You won the game!")
else:
    print("Incorrect!!! You lose the game!")
    

    
  
