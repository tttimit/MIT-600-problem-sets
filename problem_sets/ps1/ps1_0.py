out_balance = int(input("Enter the outstanding balance on your credit card: "))
interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))
min_payment_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))
total_amount_paid = 0
for i in range(1, 13):
    print("Month: " + str(i))
    current_month_payment = round(out_balance * min_payment_rate, 2)
    print("Minimum monthly payment: $" + str(current_month_payment))
    total_amount_paid += current_month_payment
    interest_paid = round(interest_rate / 12 * out_balance, 2)
    principle_paid = round(current_month_payment - interest_paid, 2)
    print("Principle paid: $" + str(principle_paid))
    out_balance = round(out_balance - principle_paid, 2)
    print("Remaining balance: $" + str(out_balance))
    #print("-----------")

print('RESULT')
print("Total amount paid: $" + str(round(total_amount_paid, 2)))
print("Remaining balance: $" + str(out_balance))
