import re
text = "cat cox cut"
result = re.findall("c.t", text)
print(result)

text = "Hello World"
print(bool(re.match(r"Hello", text)))  # True
print(bool(re.match(r"World", text)))  # False

# # 4. 0 or more (*)
text = "helloooo"
result = re.findall("lo*", text)
print(result)  # ['loooo']
# # 5. 1 or more (+)
text = "helloooo"
result = re.findall("lo+", text)
print(result)  # ['loooo']
# # 6. 0 or 1 (?)
text = "color colour"
result = re.findall("colou?r", text)
print(result)
# # 7. character sets ([ ])
text = "apple ball cat"
result = re.findall("[abc]", text)
print(result)
# # 8. Digits ([0-9])
text = "My age is 30"
result = re.findall("[0-9]", text)
print(result)  # ['3', '0']
# # alphabets [a-z]
text = "My age is 30"
result = re.findall("[a-z]", text)
print(result)
# # aplahabets [A-Z]
text = "My age is 30"
result = re.findall("[A-Z]", text)
print(result)
# # aplahabets [a-zA-Z]
text = "My age is 30"
result = re.findall("[a-zA-Z]", text)
print(result)
# # digits (\d)
text = "Marks : 90"
result = re.findall("\d", text)
print(result)  
# # non-digits (\D)
text = "Marks : 90"
result = re.findall("\D", text)
print(result)
# # not word characters (\W)
text = "Hello @ World!"
result = re.findall("\W", text)
print(result)
# # space characters (\s)
text = "Hello World!\nWelcome to Regex."
result = re.findall("\s", text)
print(result)
# # no spaces
text = "Hello World!\nWelcome to Regex."
result = re.findall("\S", text)
print(result)
# #  repetiton count
text = "phone : 4654654646546465"
result = re.findall("phone : \d{10}", text)
print(result)
# # or operator (|)
text = "cat bat rat mat"
result = re.findall("cat|rat", text)
print(result)
# # grouping ( )
text = "Mr. Smith and Mr. Johnson"
result = re.findall("Mr\. \w+", text)
print(result)

# email
text = "Contact us at test@gmail.com or admin@gmail.com"
pattern = r"[\w\.-]+@[\w\.-]+"
emails = re.findall(pattern, text)
print(emails)

