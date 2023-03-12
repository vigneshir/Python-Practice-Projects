import matplotlib.pyplot as plt

from importlib import reload
plt = reload(plt) 

plt.plot( [2,3,4,5,4], [12,4,4,63,40], "bs")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.title("Line Graph")
plt.show()
