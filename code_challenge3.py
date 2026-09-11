#POGI AKO


#Input code
sender = str(input("Sender name : "))
type = str(input("Type of item : "))
fragile = bool(input("Is the Item fragile? [yes/no] : ") =="yes")
weight = float(input("Item weight in [Kg] : "))
distance = float(input("Distance in [km] : "))
is_express = bool(input("Do you want it to be express? [yes/no] : ") =="yes")
is_international = bool(input("Do you want it to be international? [yes/no] :") =="yes")

#calculation
base_cost = (weight * 2.50) + (distance * 0.15)

#conditions

if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
	total = 0.00

elif is_international and is_express:
	total = (base_cost * 1.40) + 50.00

elif is_express or is_international and weight > 20 :
	total = (base_cost * 1.20) + 25.00

elif weight > 30 or distance > 1000 :
	total = base_cost + 30.00

else: 
	total = base_cost


#print

print("\n\n\n\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("                            RECEIPT                                     ")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print("\nName of sender: ", sender)
print("Item type: ", type)
if fragile == True :
	print("Item is : fragile")
else: 
	print("Iten is : not_fragile ")
print("Item weight: ", str(weight) + "kg")
print("Distance to Deliver: ", str(distance) + "km")
print("Is_Express : ",is_express)
print("Is_international : ",is_international)
print("Total cost: ", str(total) + "₱") 

print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
