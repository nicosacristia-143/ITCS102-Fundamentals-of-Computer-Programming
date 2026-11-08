#box
box = int(input("Number of * of your box:"))

for x in range (box):
    for y in range (box):
        if x == 0 or y == 0 or x == box - 1 or y == box - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()