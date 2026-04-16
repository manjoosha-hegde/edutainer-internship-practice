# Multithreading Demonstration Program
import threading
# Function to print numbers
def print_numbers():
    for i in range(1, 6):
        print(i)
# Function to print letters
def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(ch)
# Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
# Starting threads
t1.start()
t2.start()
# Ensuring both threads complete
t1.join()
t2.join()
print("Execution Completed")