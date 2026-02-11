# WRITE A REGEX TO VADILATE 10 DIGIT PHONE NUMBER
import re
text = "Contact: 9876543210,"
pattern = r"\b\d{10}\b"
if re.search(pattern, text):
    print("Valid 10-digit phone number found.")
else:
    print("No valid 10-digit phone number found.")


# write a regex to validate email address
# email
text = "Contact us at test@gmail.com or admin@gmail.com"
pattern = r"[\w\.-]+@[\w\.-]+"
emails = re.findall(pattern, text)
print(emails)

# extract all numbers from a given string
text = "I have 2 apples and 3 bananas."
numbers = re.findall(r"\d+", text)
print(numbers)  # Output: ['2', '3']

# validate a strong password
#   -At least 8 characters 
# one uppercase letter
# one lowercase letter
# one digit
# one special character
text = "Password123@"
pattern = r"^(?=.*[a-z])?(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
if re.match(pattern, text):
    print("Strong password.")
else:
    print("Weak password.")




# validate a pan number
text=input("enter a pan number: ")
pattern=r"^[A-Z]{5}\d{4}[A-Z]$"
pan_number=re.match(pattern,text)
if pan_number:
    print("valid pan number")
else:
  print("Invalid pan number")
pan_number =re.findall(pattern,text)
for pan_number in pan_number:
  print(pan_number)

# validate a IPV4 address
text=input("enter a IPV4 address: ")
pattern=r"^[0-9]{3}+\.[0-9]{3}+\.[0-9]{3}+\.[0-9]{3}$"
ipv4_address=re.match(pattern,text)
if ipv4_address:
    print("valid IPV4 address")
else:
  print("Invalid IPV4 address") 
ipv4_address=re.findall(pattern,text)
for ipv4_address in ipv4_address:
  print(ipv4_address)