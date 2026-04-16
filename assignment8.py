# Encapsulation and Data Protection Program
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Getter method
    def get_balance(self):
        return self.__balance
# Creating object
account = BankAccount(1000)
# Performing operations
account.deposit(500)
account.withdraw(300)
# Accessing balance using getter
print("Current Balance:", account.get_balance())