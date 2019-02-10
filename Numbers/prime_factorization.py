def check_prime(number):
    retval = True
    for num in range(2,int(number/2)):
        if number % num == 0:
            retval = False

    return retval

num = int(input("Enter a number for which you want to find the prime factors of: "))

prime_factors = []

# if num % 2 == 0:
#     prime_factors.append((2, int(num/2)))

while(num > 2):
    for factor in range(2,int(num/2)):
        if num % factor == 0 and check_prime(factor):
            prime_factors.append(factor)            
            break
    if not check_prime(num):
        num = int(num/ factor)
    else:
        break
prime_factors.append(num)
print(prime_factors)