a = [(1-x) for x in range(1, 10)]
print(a)

b = [4**i for i in range(8)]
print(b)

c = [x for x in b if x % 2 == 0]
print(c)
