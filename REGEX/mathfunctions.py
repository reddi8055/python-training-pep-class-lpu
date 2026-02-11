import math
num = 4
print (math.sqrt(num))  
print (math.pow(num, 3))
num2 = -7.8
print (math.ceil(num2))
print (math.floor(num2))
print (math.fabs(num2))


# random
import random
dice = random.randint(1, 6)
print (dice)

student = ['Alice', 'Bob', 'Charlie', 'David']
selected_student = random.choice(student)
print ("Congratulations", selected_student, "are selected")

# date and time
import datetime
current = datetime.datetime.now()
print ("Current date and time : ", current)
Today = datetime.date.today()
print ("Current date : ", Today)

year = current.year
month = current.month
day = current.day
print ("Year:", year, "Month:", month, "Day:", day)
hour = current.hour
minute = current.minute
second = current.second
print ("Hour:", hour, "Minute:", minute, "Second:", second)


birthday = datetime.date(1995, 5, 17)
age = Today.year - birthday.year - ((Today.month, Today.day) < (birthday.month, birthday.day))
print ("Age : ", age)


