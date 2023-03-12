import random
from matplotlib import pyplot

xaxis = []
yaxis = []

account = 0

for i in range(1000):
    xaxis.append(i)
    chosen_ticket = random.randint(1,10)
    winning_ticket = random.randint(1,10)
    if chosen_ticket == winning_ticket :        # pay 100 for participating, receive 1000 on winning
        account += 1000 - 100
    else:
        account -= 100
    yaxis.append(account)
  
pyplot.plot(xaxis,yaxis)
pyplot.show()    
    