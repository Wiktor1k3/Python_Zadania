import sys
lista = []
x = 0
while(x < 10):
    a = sys.stdin.readline()
    lista.append(a)
    x+=1
sys.stdout.write(str(lista))