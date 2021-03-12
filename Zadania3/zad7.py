def ciag(*a):
    b = a[1]
    c = a[2]
    a = a[0]
    print(a)
    for i in range(c-1):
        a = a*b
        print(a)

ciag(2, 3, 10)