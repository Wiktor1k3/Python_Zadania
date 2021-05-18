import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,30,0.1)
y1 = np.sin(x)
y2 = np.sin(x+np.pi)
plt.title("Wykres sin(x), cos(x)")
plt.ylabel("sin(x)")
plt.xlabel("x")
l1,l2=plt.plot(x,y1+2,"royalblue",x,y2,"darkorange")
plt.legend((l1,l2),("sin(x)","sin(x)"))
plt.show()