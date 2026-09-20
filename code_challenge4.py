#pogi ako
import getpass
print("\t\t\t\tTHIS IS LOAN.PY APP") 
print("|||||||||||||||||||||||||||||| PLEASE SIGN-UP ||||||||||||||||||||||||||||||")
username = input("enter your username: ")

print("Create a password")
password1 = getpass.getpass()
print("Enter password again")
password2 = getpass.getpass()

if password1 == password2 :
    print("\t\t\tAccount Created! Logging-in")
    print("\n\n\n|||||||||||||||||||||||||||||| LOGGED IN ||||||||||||||||||||||||||||||")
    print("Please enter your personal information to determine if you are eligible for a loan \nAny false information will result in automatic disqualification")
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    is_employed = bool(input("Are currently you employed? (Yes/No): ") == "Yes")
    if age >= 21 and age <= 65 and is_employed == True:
        job = input("Please specify your current job: ")
        credit_score = eval(input("Please enter your credit score: "))
        annual_income = eval(input("Please enter your annual income: "))
        has_collateral = bool(input("Do you have collateral? (Yes/No): ") == "Yes")
        collateral_types = ["Vehicle", "House", "Land", "Jewelry", "Stocks", "Bonds"]
        if has_collateral:
            print("note: \"anything less than 30,000 will be considered as invalid or no collateral\" \nwe would be accepting the following types of collateral: \n",collateral_types)
            type_of_collateral = input("What type of collateral do you have: ")
        else:
            has_collateral = False
        amount_of_loan = eval(input("Please enter the amount of loan you want to apply for: "))
        base_interest_rate = 0.0

    #conditional statements to determine if the user is approved for a loan and what the base interest rate will be

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

        #calculation of the total interest rate based on the base interest rate and the amount of loan
        total_interest_rate = (base_interest_rate / 100) * amount_of_loan

        #INFORMATION
        print("\n\n\n|||||||||||||||||||||||||||||| LOAN RECIEPT ||||||||||||||||||||||||||||||")
        print("Name: ", name)
        print("Age: ", age)
        print("Employed: ", is_employed)
        print("Current Job: ", job)
        print("Credit Score: ", credit_score)
        print("Annual Income: ", annual_income)
        print("Has Collateral: ", has_collateral)
        if has_collateral:
            print("Type of Collateral: ", type_of_collateral)
            print("Collateral Validity: ", "Valid" if type_of_collateral in collateral_types else "Invalid")
        print("Amount of Loan: ", amount_of_loan)
        print("Eligibility: ", "Approved" if base_interest_rate > 0 else "Rejected")
        print("Base Interest Rate: ", base_interest_rate,"%")
        print("Total Interest Rate: ", str(total_interest_rate) + "PHP")

    else:
        print("Rejected: Fails baseline criteria")

else: 
    print("password does not match, try again")

# The problem ive encountered in this code is when the line 27 is executed which is if the user has collateral 
# It turns true, but when the user inputs a type of collateral that is not in the list of collateral_types, it still considers it as valid. or it does not become false
# which is a problem because the user can input anything and it will be considered as 7.0 rather as 8.0
# another problem is if you put a condition wherein the base interest rate is at 7.0 then place like 5 zeroes 
# the calculation of it would bug like the answer is right but the decimals is wrong.
# for example: 7000.0000000001 PHP
