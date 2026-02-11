import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123456"
)
print("Connection done")
cur = conn.cursor()
cur.execute("""CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary INTEGER)""")
cur.execute("INSERT INTO employees VALUES (1, 'John Doe', 50000), (2, 'Jane Smith', 60000), (3, 'Bob Johnson', 55000), (4, 'Alice Brown', 70000), (5, 'Charlie Davis', 45000)")
cur.execute("SELECT * FROM employees")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()
cur.close()
cur = conn.cursor()
