fruits = ["Apple", "Banana","Pineapple","Mango"]
print(fruits)

num = int(input("Pick the fruit you want:"))
num1 = int(input("Pick one more:"))
fruit1 = str(input("Is there any fruit you want to add on the list? --->"))

print(fruits[num],fruits[num1])
fruits.append(fruit1)
print(fruits)

arrange =int(input("Do you want to rearrange the list \n Where do you want to put it: "))
p = str(input("Which fruit do you want:"))
fruits.insert(arrange,p)
print(fruits)

#list slicing
order = int(input("Pick fruits in order = From:"))
to = int(input("Pick fruits in order = To:"))
print(fruits[order:to])
