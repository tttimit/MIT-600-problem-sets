out_balance = int(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))
monthly_payment = 10
month = 0
remaining_balance = out_balance
while remaining_balance > 0:
    month += 1
    if month > 12:
        month = 1
        monthly_payment += 10
        remaining_balance = out_balance
##    if month == 1:
##        remaining_balance -= monthly_payment
##    else:
    remaining_balance = remaining_balance * (1 + annual_interest_rate/12) - monthly_payment
   
    

print("RESULT")
print("Monthly payment to pay off debt in 1 year: " + str(monthly_payment))
print("Number of months needed: " + str(month))
print("Balance: " + str(round(remaining_balance, 2)))
