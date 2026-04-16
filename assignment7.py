# Tuple Data Analysis Program

# Creating a tuple with 10 numeric values
numbers = (10, 25, 30, 45, 50, 65, 70, 85, 90, 100)

# Printing first three values
print("First three values:", numbers[:3])

# Printing last three values
print("Last three values:", numbers[-3:])

# Checking membership
num_to_check = int(input("Enter a number to check: "))

if num_to_check in numbers:
    print(num_to_check, "exists in the tuple")
else:
    print(num_to_check, "does not exist in the tuple")