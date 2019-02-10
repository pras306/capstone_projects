
principal_amount = int(input("Enter your initial mortgage amount (in dollars): "))
interest_rate = float(input("Enter the annual interest rate for mortgage: "))
interest_rate = interest_rate/12
interest_rate = interest_rate / 100
number_payments = int(input("Enter the number of payments for paying the loan: "))

cal_step1 = (1 + interest_rate) ** number_payments
cal_step2 = cal_step1 * interest_rate
cal_step3 = cal_step1 - 1

monthly_payment = (principal_amount * cal_step2)/cal_step3

print("Monthly payment for the above given data is: ${0}".format(monthly_payment))