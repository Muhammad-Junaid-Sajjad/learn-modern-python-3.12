# writing the factorial..

user_input = n = int(input("Enter a number: "))

# First, wel will list the numbers involved in the factorial

for i in range(n, 0, -1):
    print(i, end=" ")
# This will just prints out the numbers, involved in the factorial

# now we will get the logic  in action.......
n = int(input("Enter a number: "))
factorial = 1

# we will firstly list the numbers involved in the factorial

for i in range(n, 0, -1):
    print(i, end=" ")               # Printing the  numbers first
    factorial *= i               # then Multiplying them with its factorial/factor  to get the factorial

# then printing the fatorial numbers 

print(f"\nThe factorial of {n} is {factorial}")
