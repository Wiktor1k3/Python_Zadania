import numpy as np

mac1 = np.arange(6).reshape((2, 3))
print(mac1)
a = np.sin(mac1)
print(a)

mac2 = np.arange(6).reshape((2, 3))
print(mac2)
b = np.cos(mac2)
print(b)

c = a + b
print(c)