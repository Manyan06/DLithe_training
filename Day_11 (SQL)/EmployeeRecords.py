import sqlite3
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee(
      emp_id INTEGER,
      name TEXT,
      salray REAL
      )
""")
cursor.execute("INSERT INTO employee VALUES (101, 'Rahul', 50000)")
cursor.execute("INSERT INTO employee VALUES (102, 'Priya', 60000)")
conn.commit()
cursor.execute("SELECT * FROM employee")
print("Employee Records: ")
for row in cursor.fetchall():
  print(row)
conn.close()