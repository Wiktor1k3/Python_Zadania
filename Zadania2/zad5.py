import sys as system
from math import *
system.stdout.write("Podaj trzy liczy całkowite: ")
liczba1 = system.stdin.readline()
liczba2 = system.stdin.readline()
liczba3 = system.stdin.readline()

a = int(liczba1)
b = int(liczba2)
c = int(liczba3)
wynik = pow(a,b)+c

d = str(wynik)
system.stdout.write(d)
