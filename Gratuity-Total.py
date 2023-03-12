subtot = eval(input("Enter the subtotal: "))
gratrate = eval(input("Enter the gratuity rate: "))

grat = int((gratrate/100 * subtot)*100) / 100 
tot = int((subtot + grat)*100) / 100

print("Gratuity:  ", grat)
print("   Total: ", tot)