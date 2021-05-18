import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,20,1)
y = (1/x)
plt.plot(x,y,"g:>",label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) dla x[1,20]")
plt.ylim(0,1)
plt.xlim(0,20)
plt.legend()
plt.show()