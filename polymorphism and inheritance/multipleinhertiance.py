# class Teacher:
#     def teach(self):
#         print("Teaching")

# class Coder:
#     def teach(self):
#         print("Teaching")

# class Student(Teacher, Coder):
#     def result(self):
#         print("Pass")

# s = Student()
# s.result()


# class Parent:
#     def __init__(self):
#         self.__x = 10  # private variable
# class Child(Parent):
#     def show(self):
#         print(self.__x)
# obj = Child()
# obj.show()


# class Parent:
#     def __init__(self):
#         self._x = 100
# class Child(Parent):
#     def show(self):
#         print(self._x)
# obj = Child()
# obj.show()


# create a parent class person private variable __name and make a constructor for the name and then make getname to get the name
# then make a ckass student this is inherit person it has show_name() -> showing name using parent method

class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self): 
        return self.__name
class Student(Person):
    def show_name(self):
        print("Name:", self.get_name())
s1 = Student("Ramesh")
s1.show_name()


class Account:
    def __init__(self, balance):
        self._balance = balance
