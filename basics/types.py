# lists
# marks = [50,60,70,80,90]
# print (marks[0])
# marks.append(100)
# print(marks)
# marks.insert(2, 55)
# print(marks)
# a = len(marks)
# print(a)
# marks.remove(60)
# print (marks)
# marks.pop()
# print(marks)


# age = [20, 30, 40, 50]
# age.sort()
# print(age)
# age.reverse()
# print(age)
# print (max(age))
# print (min(age))
# # average of list
# average = sum(age) / len(age)
# print(average)

# 3

# city = ["delhi", "mumbai", "bangalore", "chennai"]
# print(city[2])
# city.append("kolkata")
# print(city)
# city.insert(2, "hyderabad")
# print(city)
# a = len(city)
# print(a)
# city.remove("mumbai")
# print (city)
# city.pop()
# print(city)





# tuple
# days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
# print(days[0])
# a = days.count("monday")
# print(a)
# # slicing
# print(days[0:3])
# print(len(days))
# print(days.index("saturday"))



#set
# numbers: {1, 2, 3, 4, 5, 6}
# print(numbers)
# for i in numbers:
#     print(i)
# numbers.add(7)
# numbers.update([8, 9, 10])
# print(numbers)
# numbers.remove(9)
# print(numbers)
# numbers.discard(10)
# print(numbers)


# marks = {50, 60, 70, 80, 90}
# print(marks)
# marks.add(100)
# print(marks)
# marks.update([110, 120])
# print(marks)
# a = len(marks)
# print(a)
# marks.remove(60)
# print (marks)
# marks.discard(80)
# print(marks)

















# -------------------------------------DAY 2 ----------------------------------------------
# DICTONARY 

# Student = {
#     "name": "ram",
#     "age": 20,
#     "marks": 50
# }
# print (Student)
# print (Student["name"])
# print(Student.get("age"))
# print (Student.keys())
# print (Student.values())
# print (Student.items())
# Student.update({"age": 21, "marks" : 60})
# print(Student)
# Student.pop("age")
# Student.popitem()
# print (Student)
# print (len(Student))


# dict1 = {"a": 2 , "b": 3}
# dict2 = dict1.copy()
# print (dict2)
# dict1 = {"a": 2 , "b": 3}
# dict2 = {"c": 4, "d": 5}
# dict1.update(dict2)  # dict1 = dict1 + dict2
# print(dict1)


# mobile = {
#     "name" : "samsung",
#     "model": "s23",
#     "color": "black",
#     "price": 50000

# }
# print (mobile["name"]) 
# print(mobile.get("color"))
# print (mobile.keys())
# print (mobile.values())
# print (mobile.items())
# mobile.update({"price": 60000})
# print (mobile)
# mobile.pop("color")
# print (mobile)
# mobile.popitem()
# print (mobile)












# contact = {}
# while True:
#     print("\n ---Contact Book---  ")
#     print ("1.Add contact")
#     print("2. view contact")
#     print ("3. search contact")
#     print ("4. delete contact")
#     print ("5. exit")

#     choice = input ("enter your choice: ")
#     if choice == "1":
#         name = input("enter name: ")
#         phone = input("enter phone number: ")
#         contact[name] = phone
#         print("contact added successfully")
#     # for view contact
#     elif choice == "2":
#         if contact:
#             print ("\n saved contact:")
#             for name, phone in contact.items():
#                 print(name, ":", phone)
#         else:
#             print("contact book is empty")
#     # for search contact
#     elif choice == "3":
#         name = input("enter name to search: ")
#         if name in contact:
#             print("phone number:", contact[name])
#         else:
#             print("contact not found")
# # delete contact
#     elif choice == "4" :
#         name = input("enter name to delete: ")
#         if name in contact:
#             del contact[name]    # contact.pop(name)
#             print("contact deleted successfully")
#         else:
#             print("contact not found")
#     elif choice == "5":
#         break
#     else:
#         print("invalid choice")


# Student = {}
# while True: 
#     print("\n---Student Management System---")
#     print("1. Add Student")
#     print("2. View Student")
#     print("3. Search Student")
#     print ("4. Delete Student")
#     print ("5. Exit")

#     choice = input("Enter your choice: ")
#     if choice == "1":
#         name = input("Enter student name: ")
#         roll_number = input("Enter roll number: ")
#         student = {
#             "name": name,
#             "roll_number": roll_number
#         }
#         Student[roll_number] = student
#         print("Student added successfully.")
#     elif choice == "2":
#         if Student:
#             print("\nSaved Students:")
#             for roll_number, student in Student.items():
#                 print("Roll Number:", roll_number)
#                 print("Name:", student["name"])
#                 print()
#         else:
#             print("No students found.")
#     elif choice == "3":
#         roll_number = input("Enter roll number to search: ")
#         if roll_number in Student:
#             student = Student[roll_number]
#             print("Name:", student["name"])
#         else:
#             print("Student not found.")
#     elif choice == "4":
#         roll_number = input("Enter roll number to delete: ")
#         if roll_number in Student:
#             del Student[roll_number]
#             print("Student deleted successfully.")
#         else:
#             print("Student not found.")
#     elif choice == "5":
#         break
#     else:
#         print("Invalid choice. Please try again.")













#  string manipulation
# s = "    Python programming"
# print (len(s))
# print (s[-1])
# print (s[:5])
# print (s[6:13])
# print (s.lower())
# print (s.upper())
# print (s.strip())  # remove space from start and end
# print (s.replace("Python", "Java"))
# print (s.split(" "))
# print (s.find("0"))
# print (s.count("a"))
# print (s.startswith("P"))
# print (s.endswith("g"))

# a = "abc"
# print (a.isalpha())
# b = "123"
# print (b.isdigit())

# example 2
# name = input("enter your name: ")
# print (len(name))
# print (name[-1])
# print (name[:5])
# print (name[6:13])
# print (name.lower())
# print (name.upper())
# print (name.strip())  # remove space from start and end
# # print (name.replace("Python", "Java"))
# print (name.split(" "))
# print (name.find("0"))
# print (name.count("a"))
# print (name.startswith("P"))
# print (name.endswith("g"))

s = "madam"
if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# vowel checking
# name = "adith"
# count = 0
# for ch in name:
#     if ch in "aeiou":
#         count += 1
# print(count)

s = "python"
result = ""
for ch in s:
    if ch in "aeiou":
        result += "*"
    else:
        result += ch
print(result)






#  s = "apple"
# for ch in s:
#     print(ch, ":", s.count(ch))
