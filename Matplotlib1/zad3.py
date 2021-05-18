import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,30,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
cos,sin = plt.plot(x,y1,"g",x,y2,"r")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres sin(x), cos(x)")
plt.ylim(-1,1)
plt.xlim(0,30)
plt.legend((sin,cos),("sin(x)","cos(x)"))
plt.grid(True)
plt.show()