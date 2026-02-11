import sqlite3
# connect () creates or opens database 
# connection1 = sqlite3.connect('school.db')
# print("Database created successfully")
# connection1.close()

# connection1 = sqlite3.connect('school.db')
# # cursor() --> run sql
# cur = connection1.cursor()
# print("Cursor created successfully")
# connection1.close()



# connection1 = sqlite3.connect('school.db')
# cur = connection1.cursor()
# cur.execute("CREATE TABLE student (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
# print("Table created successfully")
# connection1.commit()
# connection1.close()

# connection1 = sqlite3.connect('school.db')
# cur = connection1.cursor()
# cur.execute("INSERT INTO student (name, age) VALUES ('Alice', 20)")
# cur.execute("INSERT INTO student (name, age) VALUES ('Bob', 22)")
# connection1.commit()
# print("Data inserted successfully")
# connection1.close()

# connection1 = sqlite3.connect('school.db')
# cur = connection1.cursor()
# cur.execute("SELECT * FROM student")
# # for line by line use for loop
# # rows = cur.fetchall()
# # for row in rows:
# #     print(row)
# # for list use normal print (cur.fetchall())
# print (cur.fetchall())
# connection1.close()

# connection1 = sqlite3.connect('employee.db')
# cur2 = connection1.cursor()
# cur2.execute("CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)")
# cur2.execute("INSERT INTO employee (name, position, salary) VALUES ('John Doe', 'Manager', 75000)")
# cur2.execute("INSERT INTO employee (name, position, salary) VALUES ('Jane Smith', 'Developer', 65000)")
# connection1.commit()
# print(cur2.execute("SELECT * FROM employee").fetchall())
# connection1.close()




# ddl commands
# connection1 = sqlite3.connect('library.db')
# cur3 = connection1.cursor()
# cur3.executescript ( "
# "CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT, country TEXT);" 
# "INSERT INTO authors (id,name,country) VALUES (1,'John','USA'),(2,'Jane','Canada');"
# "ALTER TABLE authors ADD COLUMN birth_year INTEGER;" 
# "ALTER TABLE authors RENAME TO writers;" 
# "TRUNCATE TABLE writers;" 
# "DROP TABLE writers;")
# connection1.commit()
# print("Script executed successfully")
# connection1.close()

# dml commands
connection1 = sqlite3.connect('library.db')
cur3 = connection1.cursor()
cur3.executescript ("")


