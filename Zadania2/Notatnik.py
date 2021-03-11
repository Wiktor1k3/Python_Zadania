lista = [2, 3.4, "s", 4+3j]
print(lista)

lista.append(3.12)
lista.append("abc")

print(lista)

lista.insert(1,10)
print(lista)

lista.extend((2,3,4,5))
print(lista)

lista.pop(2) #usuniecie argumentu na pozycji 2(czyli 3 bo liczymy od 0)
print(lista)

lista.pop()
print(lista)

lista.remove(2) #usuwa argument który równa się 2
print(lista)

del lista[2] #usuniecie argumentu na pozycji 2(czyli 3 bo liczymy od 0)
print(lista)

lista.reverse() #obrocenie listy, teraz czyta od konca
print(lista)

#lista nowa = [5, 1.2, 1, 3, 9, 7, ]

lup = "----------Druga część:-----------"
print(lup)

#################################################################


slownik = {1: 22, 2: "abc", "a": "b", 4.6: "napis", 1: "a"}

print(slownik)


slownik[5]="napis1"
print(slownik)

slownik.pop(4.6)
print(slownik)

del slownik[2]
print(slownik)

print(slownik.keys())
print(slownik.values())

#####################################
print("-------Trzecia część-------")

#napis = input("Wprowadz napis: ")
#print(napis)
#print(type(napis))

#liczba= input("Wprowadz liczbe: ")
#print(type(liczba))

liczba = float(liczba)
print(liczba)
print(type(liczba))
liczba = int(liczba)
print(liczba)
print(type(liczba))

#####################################################

print("--------Czwarta część---------------")

#import sys as system
#system.stdout.write("Wprowadz tekst: ")
#napis = system.stdin.readline()
#system.stdout.write(napis)

#if warunek:
    #instrukcja1
    #instrukcja2
#elif warunek2:
   # instrukcja1
    #instrukcja2

#else:
   # instrukcja1
    #instrukcja2





