def check_prime(number):
    retval = True
    for num in range(2,int(number/2 + 1)):    
        if number % num == 0:
            retval = False

    return retval

def get_next_prime(number):
    is_prime = False
    while not is_prime:
        number += 1
        is_prime = check_prime(number)
    return number

answer = ''
num = 2

while answer.lower() != "no" and answer.lower() != "yes":
    answer = input("Do you want to print the next prime number? (Yes or No)")

while answer.lower() == 'yes':
    
    print(num)
    num = get_next_prime(num)

    answer = ''

    while answer.lower() != "no" and answer.lower() != "yes":
        answer = input("Do you want to print the next prime number? (Yes or No)")

    

