file = "expense.txt"
expenses = []

# load expenses
def load_data():
    try:
        f = open(file, "r")
        for line in f:
            amount, category = line.strip().split(",")
            expenses.append(int(amount))
        f.close()
    except:
        pass


# add expense
def add_expense():
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")

    expenses.append(amount)

    f = open(file, "a")
    f.write(str(amount) + "," + category + "\n")
    f.close()

    print("Expense added")


# total expense
def total_expense():
    print("Total Expense:", sum(expenses))


# main
load_data()

while True:
    print("\n1. Add Expense")
    print("2. Total Expense")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        total_expense()
    elif choice == "3":
        break
    else:
        print("Invalid choice")