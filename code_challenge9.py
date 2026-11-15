amount = int(input("Enter the loan amount:"))
loan_term = int(input("Enter the loan period in years:"))

month = loan_term * 12
monthly_interest_rate = 0.00256
remaining_loan = amount
principal = amount / month

print("Payment Schedule")
print("Month", "\t|\t","Monthly_Payment", "\t|\t", "Interest","\t|\t", "Principal","\t|\t", "Remaining loan" )
print("-" * 110)

for Month in range(1, month + 1):
  Interest = remaining_loan * monthly_interest_rate
  Monthly_Payment = principal + Interest
  remaining_loan = remaining_loan - principal
  print(f"{Month}", "\t|\t", f"${Monthly_Payment:.2f}","\t" "\t|\t", f"${Interest:.2f}","\t" "\t|\t" f"${principal:.2f}","\t" "\t|\t", f"{remaining_loan:.2f}")

print("=" * 100)
#task 2
row = int(input("Input number of rows:"))

for i in range (1,row + 1):
  for x in range (row - 1, i - 1, -1):
    print(" ", end ="")

  for x in range (2 * i - 1):
    if x == 0 or x == 2 * i - 2 or i == row:
      print("*",end ="")
    else:
      print(" ", end ="")
  print()

#task 3
row1 = int(input("Input number of rows:"))

for a in range(row1, 0, -1):
    for b in range(0, row1):
        if a == row1 or b == a - 1 or a == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()