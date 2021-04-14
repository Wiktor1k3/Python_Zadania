import numpy as np

def funkcja(n):
    a = np.diag([i for i in range(n,0,-2)],2)
    print(a)


funkcja(8)
