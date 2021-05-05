import numpy as np

a = np.arange(81).reshape((9, 9))
print(a)

b = a.reshape(1,81)
print(b)

c=a.reshape(3,27)
print(c)

#Możemy zmieniać kształt w dowolny sposób dopóki liczba
# elementów jest równa pierwotnej macierzy