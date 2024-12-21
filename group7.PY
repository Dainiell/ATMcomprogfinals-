def display_receipt(bank, user, balance, transaction):  # Print Details Here
    print(f"\n=== ATM Receipt ===\nBank Name      : {bank}\nCustomer Name  : {user}\nTransaction    : {transaction}\nBalance        : \u20b1{balance:.2f}\n-------------------------------------\nThank you for using the ATM service!")

# Enter only positive
def get_valid_number(prompt, positive=True):
    while True:
        try:
            value = float(input(prompt).strip())
            if positive and value <= 0:
                print("Enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Entered number should be positive only.")

# Check balance here
def handle_transaction(balance, choice, interest_rate):
    if choice == "1":
        print(f"\nYour current balance is: \u20b1{balance:.2f}")
        return balance, "Check Balance" 
    
    # Deposit code here
    elif choice == "2":
        deposit = get_valid_number("Deposit amount: \u20b1")
        print(f"\n\u20b1{deposit:.2f} deposited successfully!")
        return balance + deposit, "Deposit"
    
    # Withdrawal
    elif choice == "3":
        withdraw = get_valid_number("Withdrawal amount: \u20b1")
        if withdraw <= balance:
            print(f"\n\u20b1{withdraw:.2f} withdrawn successfully!")
            return balance - withdraw, "Withdraw"
        print("\nInsufficient balance.")
        return balance, "Failed Withdrawal"
    
    # Loan
    elif choice == "4":
        loan_types = {"1": "House and Lot", "2": "Car", "3": "Academic", "4": "Health"}
        print("\n".join([f"{k}. {v}" for k, v in loan_types.items()]))
        loan_type = input("Choose loan type: ").strip()
        
        if loan_type in loan_types:
            loan_amount = get_valid_number("Loan amount: \u20b1")
            months = int(get_valid_number("Enter repayment months: ", positive=True))
            interest = (loan_amount * interest_rate / 100) * months
            total = loan_amount + interest
            print(f"\nLoan Purpose: {loan_types[loan_type]}\nLoan Amount: \u20b1{loan_amount:.2f}\nInterest: \u20b1{interest:.2f}\nTotal Payment: \u20b1{total:.2f}\nMonthly Payment: \u20b1{total / months:.2f}")
            return balance, "Loan"
        print("\nInvalid loan type.")
    
    # Error print here
    else:
        print("\nInvalid choice.")
    return balance, "Invalid Transaction"

# Entering details here
def atm():
    pin = []
    name = []
    balance = 1000000
    attempts = 3
    interest_rate = 5
    
    # Fill up here Function for general
    while True:
        print("ATM 7")
        print(" 1. Register \n 2. Login \n 3. Exit")
        choice = int(input("Please select your choice: "))
        if choice == 1:
            bank = input("Enter Your Bank: ").strip()
            user = input("Enter Your Name:  ").strip()
            password = input("Create Your Pin: ").strip()
            confirm1 = input("Confirm Your Pin: ").strip()
            
            if not bank or not user or not password or not confirm1:
                print("Invalid Enter, You need to fill up.")
                continue

            if password.isdigit() and confirm1.isdigit() and password == confirm1:
                name.append(user)
                pin.append(int(password))
                print(f"Success your {bank} Account has been Confirmed")
            else:
                print("Pin did not match or invalid input.")
        
        elif choice == 2:
            # Enter here the log in 
            while attempts > 0:
                hello = input("Enter your name: ").strip()
                hello1 = input("Enter your pin: ").strip()
                hello2 = input("Enter your bank: ").strip()

                if not hello or not hello1 or not hello2:
                    print("You need to fill up the blank.")
                    continue

                if hello1.isdigit():
                    hello1 = int(hello1)
                
                for x in range(len(name)):
                    if hello == name[x] and pin[x] == hello1:
                        print("Successfully Logged in")
                        print(f"\nWelcome to {hello2}, {hello}!")
                        # Loan here
                        while True:
                            print("\nOptions:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Loan")
                            balance, transaction = handle_transaction(balance, input("Enter choice: ").strip(), interest_rate)
                            display_receipt(bank, user, balance, transaction)
                            if input("\nDo you want to use it again? (yes/no): ").strip().lower() != "yes":
                                print("\nThank you for using Group 7 ATM machine!!")
                                return
                else:
                    print("Invalid Account")

                attempts -= 1
                if attempts == 0:
                    print("\nAccount locked due to failed attempts.")
                else:
                    print(f"\nIncorrect PIN. {attempts} attempt(s) left.")
        
        elif choice == 3:
            print("Thank you for using Group 7 ATM")
            exit()
        elif choice > 3:
            print("Invalid Choice")

atm()
