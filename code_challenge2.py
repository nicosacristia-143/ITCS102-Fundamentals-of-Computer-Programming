a = 1000
b = 500
c = 200
d = 100
e = 50
f = 20
g = 10
h = 5
i = 1

bal = 169833

print("Money to Deposit -->",bal)

thousands = bal // a 
bal = bal % a

five_hundreds = bal // b
bal = bal % b

two_hundreds = bal // c
bal = bal % c 

hundreds = bal // d
bal = bal % d

fifthys = bal // e
bal = bal % e

twenties = bal // f
bal = bal % f

tens = bal // g
bal = bal % g

fives = bal // h
bal = bal % h

ones = bal // i
bal = bal % i

print("1000:",thousands)
print("500:",five_hundreds)
print("200:",two_hundreds)
print("100:",hundreds)
print("50 :",fifthys)
print("20 :",twenties)
print("10 :",tens)
print("5 :",fives)
print("1 :",ones)