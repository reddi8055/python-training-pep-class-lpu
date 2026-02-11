from collections import Counter
fruits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
count = Counter(fruits)
print(count)  

sentence = "hello world hello"
char_count = Counter(sentence)
print(char_count)

num = [1, 2, 2, 3, 4, 4, 4, 5]
num_count = Counter(num)
print(num_count)

import os
current_path = os.getcwd()
print("Current Working Directory:", current_path)

item = os.listdir()
print(item)


import os
folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")