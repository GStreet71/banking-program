def display_balance():
    print("************************")
    print(f"Your balance is ${balance:.2f}")
    print("************************")
    print("\n")

def deposit():
    amount = float(input("Enter deposit amount: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        print("************************")
        print(f"${amount:.2f} was deposited successfully")
        print("************************")
        print("\n")
        return amount

def withdraw():
    amount = float(input("Enter withdrawal amount: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    
    if amount > balance:
        print("************************")
        print("Insufficient funds")
        print("************************")
        print("\n")
        return 0
    else:
        print("************************")
        print(f"${amount:.2f} was withdrawn successfully")
        print("************************")
        print("\n")
        return amount

balance = 0
is_running = True

while is_running:
    print("     Banking Program    ")
    print("************************")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Make your selection (1-4): ")

    if choice == "1":
        display_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        input("Please make a valid selection: ")

print("************************")
print("Thank you! Have a nice day.")
print("************************")
print("\n")