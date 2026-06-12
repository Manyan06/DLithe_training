import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
#Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee(
  Emp_ID INTEGER PRIMARY KEY,
  Name TEXT,
  Dept_ID INTEGER
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Dep artment(
  Dept_ID INTEGER PRIMARY KEY,
  Dept_Name TEXT
)
""")
# Insert data
cursor.execute("INSERT OR IGNORE INTO Employee VALUES(1,'Amit',101)")
cursor.execute("INSERT OR IGNORE INTO Employee VALUES(2,'Neha',102)")
cursor.execute("INSERT OR IGNORE INTO Employee VALUES(3,'Ravi',103)")
cursor.execute("INSERT OR IGNORE INTO Department VALUES(101,'HR')")
cursor.execute("INSERT OR IGNORE INTO Department VALUES(102,'IT')")
conn.commit()
#LEFT JOIN
query = """SELECT Employee.Name, Department.Dept_Name FROM Employee LEFT JOIN Department On Employee.Dept_ID = Department.Dept_ID"""
cursor.execute(query)
print("Employement Fepartment Details")
for row in cursor.fetchall():
  print(row)
conn.close()