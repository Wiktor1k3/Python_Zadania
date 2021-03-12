import random

a = random.randint(-100, 100)
b = random.randint(-100, 100)
c = random.randint(-100, 100)
d = random.randint(-100, 100)
e = random.randint(-100, 100)
f = random.randint(-100, 100)
g = random.randint(-100, 100)
h = random.randint(-100, 100)
i = random.randint(-100, 100)
j = random.randint(-100, 100)

lista = [a, b, c, d, e, f, g, h, i, j]
print(lista)

p = [x for x in lista if x % 2 == 0]
print(p)
