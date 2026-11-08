#diamond

rows = int(input("Input how many rows:"))

for i in range (1, rows + 1):
    print(" " * (rows - i) + "*" * (i*2 - 1)) 


for i in range (rows-1, 0, -1):
    print(" " * (rows - i) + "*" * (i*2 - 1)) 