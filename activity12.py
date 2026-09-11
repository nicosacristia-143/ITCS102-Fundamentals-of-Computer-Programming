#multiple elif conditions

name = input("Enter your name --> ")
age = int(input("Enter your age --> "))

if age >= 0 and age <= 5 :
  print("Is an infant")

elif age >= 6 and age <= 12 :
  print("Bro is an ipadkid")

elif age >= 13 and age <= 15 :
  print("Bro is a teen")

elif age >= 16 and age <= 19 :
  print("touch some grass bro")

elif age >= 20 and age <= 29 :
  print("Go get a job")

elif age >= 30 and age <= 50 :
  print("Is a senior")

elif age >= 51 and age <= 99 :
  print("Is bro the goat?")

elif age >= 100 and age <= 200 :
  print("Ayo get some rest gang")

else: 
  print("Bro broke the world record")