out_balance = int(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))
#monthly_payment = 0.01
lower_bound = out_balance / 12
higher_bound = (out_balance * (1 + (annual_interest_rate / 12) ** 12)) / 12
monthly_payment = (lower_bound + higher_bound) / 2
month = 0
remaining_balance = out_balance
while abs(remaining_balance) > 0.1:
    month += 1
    if month > 12:
        print("remaining_balance is :" + str(round(remaining_balance,2)) + " monthly_payment is: " + str(round(monthly_payment, 2)))
        month = 1
        #if remaining_balance > 0:
        monthly_payment += (higher_bound - monthly_payment) / 2
##        else:
##            monthly_payment = (monthly_payment + lower_bound) / 2
        remaining_balance = out_balance
    remaining_balance = remaining_balance * (1 + annual_interest_rate/12) - monthly_payment
    

print("RESULT")
print("Monthly payment to pay off debt in 1 year: " + str(round(monthly_payment, 2)))
print("Number of months needed: " + str(12))
print("Balance: " + str(round(remaining_balance, 2)))
