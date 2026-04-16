# Student Result Evaluation System

# Taking input from user
marks = float(input("Enter student's marks: "))

# Checking grade using conditional statements
if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 40:
    grade = 'D'
else:
    grade = 'Fail'

# Displaying result
print("Grade:", grade)

# Pass/Fail condition
if marks >= 40:
    print("Status: Passed")
else:
    print("Status: Failed")