import numpy as np

def funkcja(n):
    tablica = np.arange(n*n)
    a = 2
    for liczba in tablica:
        tablica[liczba] = a
        a = a*2
    return tablica

print(funkcja(2))