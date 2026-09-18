#pogi ako
import getpass
print("\t\t\t\t\bTHIS IS LOAN.PY APP") 
print("|||||||||||||||||||||||||||||| PLEASE SIGN-UP ||||||||||||||||||||||||||||||")
username = input("enter your username: ")

print("Create a password")
password1 = getpass.getpass()
print("Enter password again")
password2 = getpass.getpass()

if password1 == password2 :
    print("\t\t\tAccount Created! Logging-in")
    print("\n\n\n|||||||||||||||||||||||||||||| LOGGED IN ||||||||||||||||||||||||||||||")

else: 
    print("password does not match, try again")


age = int(input("Please enter your age: "))
is_employed = bool(input("Are currently you employed? (Yes/No): ") == "Yes")
job = input("What is your current job? ")
credit_score = eval(input("Please enter your credit score: "))
annual_income = eval(input("Please enter your annual income: "))
has_collateral = bool(input("Do you have collateral? (Yes/No): ") == "Yes")
base_interest_rate = 0.0

#conditional statements to determine if the user is approved for a loan and what the base interest rate will be
if age >= 21 and is_employed == True:
    if credit_score >= 750:
        if annual_income >= 100000:
            base_interest_rate = 4.5
            print("You are approved! current base interest is: ", base_interest_rate, "%")
        else:
            base_interest_rate = 5.0
            print("You are approved! current base interest is: ", base_interest_rate, "%")  
    elif credit_score >= 600 and credit_score < 750:
            if has_collateral :
                base_interest_rate = 7.0
                print("You are approved! current base interest is: ", base_interest_rate, "%")
            elif annual_income < 40000 :
                base_interest_rate = 9.5
                print("You are approved! current base interest is: ", base_interest_rate, "%")
            else:
                base_interest_rate = 8.0
                print("You are approved! current base interest is: ", base_interest_rate, "%")
    else:        
        credit_score < 600
        print("Rejected: Credit score too low")
else:
    print("Rejected: Fails baseline criteria")

#INFORMATION
print("\n\n\n|||||||||||||||||||||||||||||| LOAN RECIEPT ||||||||||||||||||||||||||||||")
print("Username: ", username)
print("Age: ", age)
print("Employed: ", is_employed)
print("Current Job: ", job)
print("Credit Score: ", credit_score)
print("Annual Income: ", annual_income)
print("Has Collateral: ", has_collateral)
print("Eligibility: ", "Approved" if base_interest_rate > 0 else "Rejected")
print("Base Interest Rate: ", base_interest_rate, "%")