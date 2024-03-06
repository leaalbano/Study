'''Problem 2: Bank Account Class
Create a Python class named BankAccount with the following attributes:

account_number (string)
account_holder (string)
balance (float)
Include methods in the class to:

Deposit money into the account.
Withdraw money from the account.
Print the account details.'''

#Class object
class BankAccount:
    
    #class constructor
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    #methods
    def deposit(self, amount):
        if amount < 0:
            return self.balance
        else:
            self.balance += amount
            return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"${amount} can't be more than balance. Current balance is ${self.balance}")
            return self.balance
        elif amount <= 0:
            return self.balance
        else:
            self.balance -= amount
            return self.balance

    def print_details(self):
        print("Account number: ", self.account_number)
        print("Account holder: ", self.account_holder)
        print(f"Balance: ${self.balance}")


