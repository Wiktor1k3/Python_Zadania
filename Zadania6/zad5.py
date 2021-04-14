import numpy as np

def funkcja(n):
    wektor = np.diag([i for i in range(8,0,-2)],2)
    print(wektor)


funkcja(8)