# Nested Condition Demonstration

# Taking input from user
num = int(input("Enter a number: "))

# Checking conditions
if num > 0:
    print("The number is positive")
    
    # Nested condition
    if num % 2 == 0:
        print("It is even")
    else:
        print("It is odd")
else:
    print("The number is not positive")