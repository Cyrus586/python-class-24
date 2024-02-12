

# EXAMPLE 1
# 
print("-----------------------------")
print("Select an option")
print("A: Withdraw money")
print("B: Deposit money")

user_option = input("Enter your option: ")

print("-----------------------------")

if (user_option == "a" or user_option == "A"):
    withdraw = float(input("Enter amount to be withdrawn: "))
    account_balance = int(input("Enter the current amount in your bank account: "))
    
    def subtract_amount(withdraw, account_balance):
        result = account_balance - withdraw 
        print("Your new account balance is: ", result)
        print(str(account_balance) + " - " + str(withdraw) + " = " + str(result) + "Shs. " )
        print("------------------")
    subtract_amount(withdraw, account_balance)
    
elif user_option == "b" or user_option == "B":
    deposit = float(input("Enter amount to be deposited: "))
    account_balance = account_balance = int(input("Enter the current amount in your bank account: "))
    
    def add_amount(deposit, account_balance):
        result = account_balance + deposit
        print("Your new account balance is: ", result)
        print(str(deposit) + " + " + str(account_balance) + " = " + str(result) + "Shs.")
    add_amount(deposit, account_balance)

else:
    print("Something went wrong, you might have entered a wrong option:", user_option)


# EXAMPLE 2
def deposit(balance, amount):
    "Function to deposit money"
    balance += amount
    return balance

def withdraw(balance,amount):
    "Function to withdraw money"
    if amount <= balance:
        balance -= amount
        return balance, True
    else:
        return balance, False

def bank_info():
    "Function for user interaction"
    balance = 0
    print("Welcome to Cyberspace Maze Bank!")
    while True:
        print("\nWhat would you like to do:")
        print("A: Deposit money")
        print("B: Withdraw money")
        print("C: Exit")
        
        choice = input("Enter your choice: ")
        if choice == "a" or choice == "A":
            amount = float(input("Enter the amount to deposit: "))
            balance = deposit(balance, amount)
            print(f"Deposit of {amount} was successful. Current balance: shs.{balance}")
        elif choice == "b" or choice == "B":
            amount = float(input("Enter the amount to withdraw: "))
            balance,  success = withdraw(balance, amount)
            if success:
                print(f"Withdraw of shs.{amount} was successful. Current Balance: shs.{balance}")
            else:
                print(f"Insufficient funds. Current balance: shs.{balance}")
        elif choice == "c" or choice == "C":
            print("Thank you for using our Bank. Goodbye")
            break
        else:
            print("Something went wrong, you might have entered a wrong option:", choice)

if __name__ == "__main__":
    bank_info()