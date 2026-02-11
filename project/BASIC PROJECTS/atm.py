file_name = 'atm_data.txt'
balance = 10000
pin = '1234'

def load_data():
    global balance, pin
    try:
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()
        pin = lines[0].strip()
        balance = int(lines[1].strip())
    except:
        save_data()

def check_balance():
    print("Your balance is:", balance)

def save_data():
    file = open(file_name, "w")
    file.write(pin + "\n")
    file.write(str(balance))
    file.close()

def deposit_money():
    global balance
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Enter a valid amount")
            return
        balance += amount
        save_data()
        print("Money deposited successfully")
    except ValueError:
        print("Please enter numbers only")

def withdraw_money():
    global balance
    try:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Enter a valid amount")
        elif amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            save_data()
            print("Please collect your cash")
    except ValueError:
        print("Please enter numbers only")

def change_pin():
    global pin
    old_pin = input("Enter the old PIN: ")
    
    if old_pin == pin:
        new_pin = input("Enter your new PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            save_data()
            print("PIN changed successfully")
        else:
            print("PIN must be 4 digits")
    else:
        print("Incorrect old PIN")

def main():
    load_data()
    
    user_pin = input("Enter the PIN: ")
    if user_pin != pin:
        print("Incorrect PIN")
        return
    
    while True:
        print("\n.......ATM MENU.........")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")

main()