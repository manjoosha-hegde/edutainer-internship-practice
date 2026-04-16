# List-Based Data Management Program

# Step 1: Create a list of five students
students = ["Asha", "Rahul", "Kiran", "Neha", "Vikram"]

print("Original List:", students)

# Step 2: Add a new student
students.append("Sneha")
print("After Adding a Student:", students)

# Step 3: Remove a student
students.remove("Kiran")
print("After Removing a Student:", students)

# Step 4: Sort the list
students.sort()
print("Sorted List:", students)

# Step 5: Create another list and concatenate
new_students = ["Arjun", "Pooja", "Ramesh"]
combined_list = students + new_students

print("Combined List:", combined_list)