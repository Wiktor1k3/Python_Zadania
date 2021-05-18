import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,20,1)
y = (1/x)
plt.plot(x,y,label="f(x)")
plt.ylim(0,1)
plt.xlim(0,20)
plt.legend()
plt.show()