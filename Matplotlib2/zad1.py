import numpy as np
import matplotlib.pyplot as plt

t = plt.figure()
c = t.gca(projection='3d')

z = np.linspace(0, 2*np.pi)
x = np.sin(z)
y = 2*np.cos(z)
c.plot(x, y, z)
c.legend()
plt.show()