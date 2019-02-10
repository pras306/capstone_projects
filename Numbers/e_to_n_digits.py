import math

def roundoff(num, limit):
    strlist = str(num)[0:limit + 2]
    return strlist


digit = int(input("Enter how many digits of e you wish to see? "))

if digit > 15:
    print("Program has an upper limit to print till 15 digits only")
    digit = 15
num = math.e

result = roundoff(num,digit)

print("The value of e to the {0} digit is: {1}".format(digit, result))




