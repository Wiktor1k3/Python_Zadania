with open("c.txt","w") as pliczek:
    for x in range(5) :
        pliczek.write("Coś\n")
with open("c.txt","r") as pliczek:
    for d in pliczek:
        print(d, end="")