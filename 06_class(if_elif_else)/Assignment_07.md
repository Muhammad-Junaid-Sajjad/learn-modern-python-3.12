# Python Assignment No.07 
 ## Hi there! 
#### Now we will be breaking down the whole Assignment into small chunks along with its results 
#### No output means that the code is done interpreted (compiled by python interpreter)

## Step 1 :
#### we will prompt the user to enter the their name 
``` python
name: str = input("Enter your name: ")

# no output here 
``` 

## Step 2: Prompt the user to enter three favorite numbers
#### we will be Converting  the input strings to integers and store them in a list
```python
favorite_numbers: list[int] = [
    int(input("Enter your first favorite number: ")), 
    int(input("Enter your second favorite number: ")), 
    int(input("Enter your third favorite number: "))

# no output here 
```
## Step 3: Greet the user
#### we will greet the user and store our input number () using if_else statement 
``` python 
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# output here :

Hello, Junaid! Let's explore your favorite numbers:
```
## Step 4: Check if the numbers are even or odd
#### we will Store the results in a list of tuples and store our input number () using if_else statement 
```python
even_odd_list: list[tuple[int, str]] = []
for number in favorite_numbers:
    if number % 2 == 0:
        even_odd_list.append((number, "even"))
        print(f"The number {number} is even.")
    else:
        even_odd_list.append((number, "odd"))
        print(f"The number {number} is odd.")

# output here : 

The number 4 is even.
The number 6 is even.
The number 9 is odd.

```
## Step 5: Print the numbers and their squares
#### we will be Using a for loop to iterate through the favorite_numbers list
```python
for number in favorite_numbers:
    square: tuple[int, int] = (number, number ** 2)
    print(f"The number {number} and its square: {square}")

# output here : 

The number 4 and its square: (4, 16)
The number 6 and its square: (6, 36)
The number 9 and its square: (9, 81)

```
## Step 6: Calculate the sum of the three favorite numbers
#### we will be calculating the total sum of given numbers 
```python
sum_numbers: int = sum(favorite_numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}")

# output here :


Amazing! The sum of your favorite numbers is: 19

```
## Step 7: Check if the sum is a prime number without using a function
#### Since, A prime number has no divisors other than 1 and itself so we will use create & use a simple logic 
#### to check if the sum of the given numbers in previous steps is prime or not 
```python
# Step 7a: Assume the number is prime initially
is_prime: bool = True

# Step 7b: A prime number should be greater than 1
if sum_numbers < 2:
    is_prime = False
else:
    # Step 7c: Check if the sum has any divisors other than 1 and itself
    for i in range(2, sum_numbers):
        if sum_numbers % i == 0:
            is_prime = False
            break
# no output here :
```
## Step 8: Notify the user if the sum is a prime number or not
#### In this last step we will just print out message for users using if_else statement & print the  number gotten from sum in step-7 is prime or not 
```python
if is_prime:
    print(f"Wow, {sum_numbers} is a prime number!")
else:
    print(f"{sum_numbers} is not a prime number.")

# output here : 

Wow, 19 is a prime number!

```

## You can se te whole assignment, just clicking to this link 
[Assignment_07_repo link ] (https://github.com/Muhammad-Junaid-Sajjad/learn-modern-python-3.12/blob/main/06_class(if_elif_else)/Assignment_07.ipynb)

## You can also view it here as an image 
[Github Repo Image](https://github.com/Muhammad-Junaid-Sajjad/learn-modern-python-3.12/blob/main/06_class(if_elif_else)/Assignment_07.ipynb)

