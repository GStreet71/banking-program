# Parent Class: User
# Holds details about user
# Has function to show user details
# Child Class: bank
# Stores details about the account balance
# Stores details about the amount
# Allows for deposits, withdrawals, view_balance

# Parent Class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print("\nPersonal Details")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"${self.amount} has successfully been deposited. Your account balance is ${self.balance}")
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Available Balance: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print(f"${self.amount} has successfully been withdrawn. Your account balance is ${self.balance}")

    def view_balance(self):
        self.details()
        print(f"Account Balance is ${self.balance}")

tre = Bank("Tra'Devian LaCartier Miller", 23, "Male")

tre.deposit(200)
tre.deposit(300)
tre.deposit(500)
tre.withdraw(62)
tre.withdraw(562)
tre.view_balance()
