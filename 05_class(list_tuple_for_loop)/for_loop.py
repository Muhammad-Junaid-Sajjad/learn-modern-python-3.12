# Define the numbers for which we want to create multiplication tables
numbers = [2, 7, 11]

# Loop through each number in the list
for number in numbers:
    # Print a header for the current multiplication table
    print(f"Multiplication Table for {number}:")

    # Loop from 1 to 10 to create the table
    for i in range(1, 11):
        # Calculate the product
        product = number * i

        # Print the current line of the table
        print(f"{number} x {i} = {product}")

    # Print a blank line to separate tables
    print()
