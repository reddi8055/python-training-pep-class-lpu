# file = open("data.txt", "mode-> r,w,a")  r- read w- write a - append
# file=open("student.txt","w")
# file.write("Name: Ramesh\n")
# file.write("Age: 20\n")
# file.close()

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("student.txt", "a")
# file.write("City: Delhi\n")
# file.close()

# file = open("student.txt", "r")
# # data = file.readline()
# data = file.readlines()
# print(data)
# file.close()


# file = open ("personal.txt" , "w")
# file.write("Name: Ramesh\n")
# file.write("Age: 20\n")
# file.close()

# file = open("personal.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("personal.txt", "a")
# file.write("City: Delhi/n")
# file.close()

# file = open("personal.txt", "r")
# # data = file.readline()
# data = file.readlines()
# print(data)
# print("characters in file:", len(data))
# words = data.split()
# print("words in file:", len(words))
# file.close()
 


# file = open("student.txt", "r")
# data = file.read()
# count=data.lower().count("a")
# print("word count:", count)
# file.close()

# file = open("student.txt", "r")
# data = file.read()
# # replace
# data = data.replace("Ramesh", "Rahul")
# file.close()
# file = open("student.txt", "w")
# file.write(data)
# file.close()

file = open("movies.txt", "r")
data = file.read()
print(data[:10])
file.close()


try:
    a = int(input("enter a number: "))
    b = int(input("enter another number: "))
    print(a / b)
except :
    print("invalid input")

    