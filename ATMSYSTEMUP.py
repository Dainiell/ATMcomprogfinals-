def display_receipt(bank, user, balance, transaction):  #Print Details Here
    print(f"\n=== ATM Receipt ===\nBank Name      : {bank}\nCustomer Name  : {user}\nTransaction    : {transaction}\nBalance        : ₱{balance:.2f}\n-------------------------------------\nThank you for using the ATM service!")

#Enter only positive
def get_valid_number(prompt, positive=True):
    while True:
        try:
            value = float(input(prompt))
            if positive and value <= 0:
                print("Enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Entered number should be positive only.")  

#check balanced here
def handle_transaction(balance, choice, interest_rate):
    if choice == "1":
        print(f"\nYour current balance is: ₱{balance:.2f}")
        return balance, "Check Balance" 
    
 #deposit code here
    elif choice == "2":
        deposit = get_valid_number("Deposit amount: ₱")
        print(f"\n₱{deposit:.2f} deposited successfully!")
        return balance + deposit, "Deposit"
    
   #Withdrawal
    elif choice == "3":
        withdraw = get_valid_number("Withdrawal amount: ₱")
        if withdraw <= balance:
            print(f"\n₱{withdraw:.2f} withdrawn successfully!")
            return balance - withdraw, "Withdraw"
        print("\nInsufficient balance.")
        return balance, "Failed Withdrawal"
    
    #loan
    elif choice == "4":
        loan_types = {"1": "House and Lot", "2": "Car", "3": "Academic", "4": "Health"}
        print("\n".join([f"{k}. {v}" for k, v in loan_types.items()]))
        loan_type = input("Choose loan type: ")
       
        if loan_type in loan_types:
            loan_amount = get_valid_number("loan amount: ₱")
            months = int(get_valid_number("Enter repayment months: ", positive=True))
            interest = (loan_amount * interest_rate / 100) * months
            total = loan_amount + interest
            print(f"\nLoan Purpose: {loan_types[loan_type]}\nLoan Amount: ₱{loan_amount:.2f}\nInterest: ₱{interest:.2f}\nTotal Payment: ₱{total:.2f}\nMonthly Payment: ₱{total / months:.2f}")
            return balance, "Loan"
        print("\nInvalid loan type.")
    
    #error print here
    else:
        print("\nInvalid choice.")
    return balance, "Invalid Transaction"

#Entering details here
def atm():
    pin =[]
    name = []
    balance = 1000000
    attempts = 3
    interest_rate = 5
    
    #fillup here Funtion for general
    while True:
        print ("ATM 7")
        print(" 1. Register \n 2. Login \n 3. Exit")
        choice = int(input("Please select your choice: "))
        if choice == 1:
            bank,user,password,confirm1 = input("Enter Your Bank: "), input("Enter Your Name:  "), int(input("Create Your Pin: ")), int(input("Confirm Your Pin: "))
            if  (bank,user,password,confirm1) == " ":
                if password == confirm1:
                    name.append(user)
                    pin.append(password)
                    print(f"Success your {bank} Account has been Confirm")
                else:
                    print("Pin did not match")
        elif choice == 2:
                
                #Enter here the log in 
                while attempts > 0:
                    hello = input("Enter your name: ")
                    hello1 = int(input("Enter your pin: "))
                    hello2 = input("Enter your bank: ")                    
                    while True:
                        for x in range(len(name)):
                            if hello == name[x] and pin[x] == hello1:
                                print("Successfuly Logged in ")
                                print(f"\nWelcome to {hello2}, {hello}!")
                               #loan here
                                while True:
                                    print("\nOptions:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Loan")
                                    balance, transaction = handle_transaction(balance, input("Enter choice: "), interest_rate)
                                    display_receipt(bank, user, balance, transaction)
                                    if input("\nDo you want to used it again? (yes/no): ").strip().lower() != "yes":
                                            print("\nThank you for using Group 7 ATM machine!!")
                                            return
                                     #error handling if 3 attempts is waste by entering the passcode   
                                    elif attempts == 0:
                                        print("\nAccount locked due to failed attempts.")   
                                    else:
                                        attempts -= 1
                                        print(f"\nIncorrect PIN. {attempts} attempt(s) left.")
                        else:
                                print("Invalid Account")
                                print("Pleased Try Again")
                                atm()
          #Statement apology                      
        elif choice == 3:
            print("Thankyou for using Group 7 ATM")
            exit()
        elif choice > 3 :
            print("Invalid Choice")
        
atm()
