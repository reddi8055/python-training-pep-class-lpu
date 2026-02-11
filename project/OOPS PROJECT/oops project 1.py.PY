# the system should calculate salary for different types of empolyees using all oops concepts

# Empolyee - Abstract class
# full time employee - child class
# part time employee - child class
# salary - encapsulated data
# payroll system - controller(HAS - A)
# output -

# Empolyee created
# Salary: 50000
# Empolyee Created
# Salary: 40000

# class BankAccount:
#     def __init__(self, acc_no, name, balance):   # parametrized constructor
#         self.acc_no = acc_no
#         self.name = name
#         self._balance = balance
#     def desposit(self, amount):
#         self._balance += amount
#         return self._balance
#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount
#             return self._balance
#         else:
#             return "Insufficient balance"
#     def get_balance(self):
#         return self._balance
#     def calculate_intrest(self):
#         pass
# class SavingAccount(BankAccount):
#     def calculate_intrest(self):
#         intrest = self._balance * 0.04
#         return intrest
# class CurrentAccount(BankAccount):
#     def calculate_intrest(self):
#         return 0
# class BankApp:
#     def __init__(self):
#         self.account = None
#     def create_account(self, acc_no, name, balance, acc_type):
#         if acc_type == "savings":
#             self.account = SavingAccount(acc_no, name, balance)
#         else:
#             self.account = CurrentAccount(acc_no, name, balance)
#         return "Account created successfully"
#     def deposit_money(self, amount):
#         return self.account.desposit(amount)
#     def withdraw_money(self, amount):
#         return self.account.withdraw(amount)
#     def check_balance(self):
#         return self.account.get_balance()
#     def get_intrest(self):
#         return self.account.calculate_intrest()
# app = BankApp()
# print(app.create_account(101, "Alice", 1000, "savings"))
# print("Balance after deposit:", app.deposit_money(500))
# print("Balance after withdrawal:", app.withdraw_money(300))
# print("current balance:", app.check_balance())
# print("Interest earned:", app.get_intrest())


# the system should calculate salary for different types of empolyees using all oops concepts

# Empolyee - Abstract class
# full time employee - child class
# part time employee - child class
# salary - encapsulated data
# payroll system - controller(HAS - A)
# output -

# Empolyee created
# Salary: 50000
# Empolyee Created
# Salary: 40000











# class Employee:
#     def __init__(self,emp_id, name):
#         self.emp_id = emp_id
#         self.name = name
#     def calculate_salary(self):
#         pass
# class FullTimeEmployee(Employee):
#     def __init__(self, emp_id, name, monthly_salary):
#         super().__init__(emp_id, name)
#         self.__monthly_salary = monthly_salary  # encapsulated data
#     def calculate_salary(self):
#         return self.__monthly_salary
# class PartTimeEmployee(Employee):
#     def __init__(self, emp_id, name, hourly_rate, hours_worked):
#         super().__init__(emp_id, name)
#         self.__hourly_rate = hourly_rate
#         self.__hours_worked = hours_worked
#     def calculate_salary(self):
#         return self.__hourly_rate * self.__hours_worked
# class PayrollSystem:
#     def __init__(self):
#         self.empolyee = None
#     def add_employee(self, empolyee):
#         self.empolyee = empolyee
#     def calculate_salary(self):
#         return self.empolyee.calculate_salary()
# payroll = PayrollSystem()
# ft_emp = FullTimeEmployee(1, "John Doe", 50000)
# payroll.add_employee(ft_emp)
# print("Empolyee created")

# print("Salary:", payroll.calculate_salary())
# pt_emp = PartTimeEmployee(2, "Jane Smith", 20, 2000)
# payroll.add_employee(pt_emp)
# print("Empolyee Created")
# print("Salary:", payroll.calculate_salary())






# design a console based library management system


# a libaray item is the base(abstact) idea
# book and maganixe are different type of items
# borrowing rules behave diff for each of them
# a liabraryApp contoroles items (HAS_A)
# use oops concepts and return value,  not only prints
class libraryitem:
    def _init_(self,days):
        self.days=days
    def book_charge(self): # Method will be overriden 
        pass

class Book(libraryitem): #Inheritance
    def book_charge(self): 
        return self.days * 10
class Magzine(libraryitem):
    def book_charge(self):
        return self.days * 10

class LibraryApp: #HAS-A Relation 
    def _init_(self, name, days):
        self.name = name
        self.item_obj = Book(days)  

    def show(self):
        print("Item Type:", self.name)
        print("Days borrowed:", self.item_obj.days)
        print("Total Charge:", self.item_obj.book_charge())

app = LibraryApp("Book", 8)
app.show()









