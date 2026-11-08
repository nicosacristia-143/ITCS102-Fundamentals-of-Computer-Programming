size = int(input("Size of your (X) character:"))

for x in range (size):
    for y in range (0,size):
        if x + y == size-1 or x == y:
            print("*", end = " ")
        else:
            print(" ", end= " ")
    print()