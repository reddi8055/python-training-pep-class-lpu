# QUESTION:
# Write a Python program to:
# 1. Generate 10 random integers between 1 and 100.
# 2. Separate the numbers into even and odd lists.
# 3. Round each number to the nearest multiple of 10.
# 4. Count the occurrences of each number.
# 5. Store all the results in a text file named "project_results.txt".

import random
import math

# generate random numbers
lst = [random.randint(1, 100) for _ in range(10)]

# check even and odd
even = []
odd = []
for n in lst:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

# round numbers to nearest 10
rounded = [round(n / 10) * 10 for n in lst]

# count occurrences
count = {}
for n in lst:
    count[n] = count.get(n, 0) + 1

# save results to file
fs = open("project_results.txt", "w")
fs.write("Numbers: " + str(lst) + "\n")
fs.write("Even: " + str(even) + "\n")
fs.write("Odd: " + str(odd) + "\n")
fs.write("Rounded: " + str(rounded) + "\n")
fs.write("Count:\n")

for k, v in count.items():
    fs.write(f"{k}: {v}\n")

fs.close()



































# 1. generate random password
# 2. check password strength
# 3. count characters in password
# 4. calculate strength score using math
# 5. save result in a file using os

import random
import math
import os

# characters manually defined
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
specials = "!@#$%^&*()_+"
all_chars = letters + digits + specials

# generate password
password = ""
for i in range(12):
    password += random.choice(all_chars)

# count characters
char_count = {}
for ch in password:
    char_count[ch] = char_count.get(ch, 0) + 1

# check strength
upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper = True
    elif ch in "abcdefghijklmnopqrstuvwxyz":
        lower = True
    elif ch in digits:
        digit = True
    elif ch in specials:
        special = True

strength = upper + lower + digit + special

# strength score using math
score = round(math.log(len(password)) * strength, 2)

# save result using os
os.makedirs("output", exist_ok=True)
f = open("output/password.txt", "w")
f.write("Password: " + password + "\n")
f.write("Character Count: " + str(char_count) + "\n")
f.write("Strength Score: " + str(score))
f.close()

print("Password saved in output/password.txt")
