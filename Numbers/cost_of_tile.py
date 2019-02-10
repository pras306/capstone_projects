import re

cost = int(input("Enter the cost of tiles (in dollars): "))
width = int(input("Enter width of floor (in feet): "))
height = int(input("Enter height of floor (in feet): "))
total_cost = width * height * cost

print("The cost of tiles of {0} x {1} floor is ${2}".format(width, height, total_cost))
