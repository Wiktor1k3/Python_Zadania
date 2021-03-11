from math import *

pierwsza_liczba = input("Podaj pierwszą liczbę: ")
znak = input("Podaj znak działania: ")
druga_liczba = input("Podaj drugą liczbę: ")

 if znak == "+":
    suma = int(pierwsza_liczba) + int(druga_liczba)
    print(suma)
 elif znak == "-":
    roznica = int(pierwsza_liczba) - int(druga_liczba)
    print(roznica)
 elif znak == "*":
    iloczyn = int(pierwsza_liczba) * int(druga_liczba)
    print(iloczyn)
 elif znak == "/":
    iloraz = int(pierwsza_liczba) / int(druga_liczba)
    print(iloraz)
 else:
    print("error")
