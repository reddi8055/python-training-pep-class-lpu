# take input print its type and then print double of it
a = int(input("enter a number: "))
print (type(a))
print (a * 2)


# take input salary as string then convert it into int and add bonus 5000 and print total salary
salary = input("enter your salary: ")
total_salary = int(salary) + 5000
print(total_salary)

# print hot cold
temp = int(input("enter the temperature: "))
if (temp > 30):
    print("hot")
else:
    print("cold")


# print table of a number and also counr how many numbers are printed
num = int(input("enter a number: "))
count = 0
for i in range(1, 11):
    print(num * i)
    count += 1
print(count)
 
# take a number and reverse it 
number = int(input("enter a number: "))
reverse = 0
while (number > 0):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print(reverse)

# check even odd using function
def evenodd (num):
    if (num % 2 == 0):
        return "even"
    else:
        return "odd"
a = int(input("enter a number: "))
result = evenodd(a)
print(result)

# create a lambda function to find cube of a number
cube = lambda x: x * x * x
print(cube(2))
