lista = [x for x in range(0, 31)]
lista2 = [str(x*2) for x in lista]
plik = open("pomx2.txt", "w")
plik.writelines(lista2)