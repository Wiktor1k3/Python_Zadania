import numpy as np

a = np.array([[1,6,3],[7,3,2],[1,8,3]])
print(a)
b = np.arange(16).reshape((4, 4))
print(b)

print("Najmniejsze liczby w a:",a.min(axis=0))
print("Największe liczby w a:", a.max(axis=1))
print("Najmniejsze liczby w b:",b.min(axis=0))
print("Największe liczby w b:", b.max(axis=1))