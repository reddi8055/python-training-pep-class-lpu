# class Payment:
#     def pay(self, amount):
#         pass
# # as we can see above the method is present but it is not completed the child class has to implement it
# class UPI(Payment):
#     def pay(self, amount):
#         print("Paid using UPI:", amount)
# obj = UPI()
# obj.pay(12)
# class Card(Payment):
#     def pay(self,amount):
#         print("Paid using the Card: ", amount)
# obj = Card()
# obj.pay(15)

# class Cash(Payment):
#     def pay(self, amount):
#         print("Paid using Cash: ", amount)
# obj = Cash()
# obj.pay(20)
# # here we have created three child classes that have implemented the pay method













# example 2
# here we have created an abstract class shape with an abstract method area
# and three child classes that have implemented the area method for different shapes

# class Shape :
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def area(self, length, breadth):
#         return length * breadth
# obj = Rectangle()
# print("Area of Rectangle: ", obj.area(5, 10))
# class Circle(Shape):
#     def area(self, radius):
#         return 3.14 * radius * radius
# obj = Circle()
# print("Area of Circle: ", obj.area(5))
# class Square(Shape):
#     def area(self, side):
#         return side * side
# obj = Square()
# print("Area of Square: ", obj.area(5))













# ABSTARCTION AND INTERFACES IN PYTHON
# ABSTRACTION EXAMPLE 
# class Animal:
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# dog = Dog()
# cat = Cat()
# print(dog.sound())
# print(cat.sound())

# # INTERFACE EXAMPLE
# class AnimalInterface:
#     def sound(self):
#         pass
# class Dog(AnimalInterface):
#     def sound(self):
#         return "Bark"
# class Cat(AnimalInterface):
#     def sound(self):
#         return "Meow"
# dog = Dog()
# cat = Cat()
# print(dog.sound())
# print(cat.sound())



class Course:
    def course_info(self):
        pass
    def course_duration(self):
        pass
class ExamInterface:
    def exam_type(self):
        pass    
class PythonCourse(Course, ExamInterface):
    def course_info(self):
        return "Python Programming"
    def course_duration(self):
        return "3 months"
    def exam_type(self):
        return "Online"
python_course = PythonCourse()
print(python_course.course_info())
print(python_course.course_duration())
print(python_course.exam_type())