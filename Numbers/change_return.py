
cost = float(input("Enter the total cost (in dollars): "))
amount_given = float(input("Enter the amount given by user (in dollars):"))

quarters = 0
dimes = 0
nickels = 0
pennies = 0

while cost > amount_given:
    print("User has not paid the entire amount.")
    cost = float(input("Enter the total cost (in dollars): "))

change_amount = round(amount_given - cost, 2) 

print("The change to be returned is {0}".format(change_amount))

cents = round(change_amount % 1, 2)

while(cents > 0):
    if cents >= 0.25:
        quarters += 1
        cents = round(cents - 0.25, 2)
    elif cents < 0.25 and cents >= 0.10:
        dimes += 1
        cents = round(cents - 0.10, 2)
    elif cents < 0.10 and cents >= 0.05:
        nickels += 1
        cents = round(cents - 0.05, 2)
    else:
        pennies += 1
        cents = round(cents - 0.01, 2)        
    
print("The number of quarters is {0}, dimes is {1}, nickels is {2} and pennies is {3}".format(quarters, dimes, nickels, pennies))