class Addres:
    def __init__(self,city):
        self.city = city
    def show_address(self):
        print ("city:", self.city)
#student class
class Student:
    def __init__(self,name,city):
        self.name = name
        # compostion
        # creating object of address class inside the student class
        self.address= Addres(city)
    def show_student(self):
        print("Name:",self.name)
        # using object of another class
        self.address.show_address
s = Student("karan", "delhi")
s.show_student()



class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()  # composition
    def start(self):
        self.engine.start()
        print("Car started")
my_car = Car()
my_car.start()
