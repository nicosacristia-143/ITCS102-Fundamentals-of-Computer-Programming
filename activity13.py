#pogi ako

age = int(input("Enter your age: "))
is_employed = bool(input("Are you currently employed? [True/False]"))
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
has_collateral = bool(input("Do you have collateral?"))

base_interest_rate = 5.0
if age >= 21 and is_employed == True :
    if credit_score >= 750:
        base_interest_rate = 5.0
        if annual_income >= 100000:
           base_interest_rate = 4.5
        print("You are eligible for a loan with a base interest rate of 4.5%.")
    elif 600 <= credit_score < 750:
        base_interest_rate = 8.0
        if annual_income >= 100000:
            print("You are eligible for a loan with a base interest rate of 8.0%.")
            base_interest_rate = 6.5
    else:
        base_interest_rate = 0.10
else:
    print("You are not eligible for a loan due to age or employment status.")