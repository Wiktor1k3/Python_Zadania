import numpy as np

def funkcja(n, m):
    a = np.logspace(1, m, num=m, base=n)
    a = a.astype(int)
    return a

print(funkcja(2, 4))