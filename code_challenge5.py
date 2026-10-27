
num = int(input("Enter a number:"))
for x in range(num,0,-1):
    for y in range(1, x):
        print("*", end = " ")
    print()

print ("==================")

for x in range(1,num,1):
    for y in range(0, x):
        print(x, end = " ")
    print()