prev_num = 1
current_num = 1

choice = 0
while(choice != 1 and choice != 2):
    print("Do you wish to generate Fibonacci sequence upto the number or to the Nth number?")
    choice = int(input("Enter 1 to generate upto the number OR 2 to generate upto Nth number: "))

limit = int(input("Enter the limit for the sequence: "))
print("{0}".format(prev_num))

if choice == 1:
    while(current_num <= limit):
        print("{0}".format(current_num))
        buffer = prev_num
        prev_num = current_num
        current_num += buffer
elif choice == 2:
    count = 2
    while (count <= limit):
        print("{0}".format(current_num))
        buffer = prev_num
        prev_num = current_num
        current_num += buffer
        count += 1
