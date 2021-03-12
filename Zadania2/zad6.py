a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
c = input("Podaj trzecią liczbę: ")

if a>b:
    if b>c:
        print("Największa liczba to:",a)
if a<b:
    if b<c:
        print("Największa liczba to:",c)
    elif b>c:
        print("Największa liczba to", b)

