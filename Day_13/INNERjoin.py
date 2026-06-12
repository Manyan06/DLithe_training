import sqlite3
conn = sqlite3.connect("college.db")
cursor = conn.cursor()
#Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
  Student_ID INTEGER PRIMARY KEY,
  Name TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Courses(
  Course_ID INTEGER PRIMARY KEY,
  Student_ID INTEGER,
  Course_Name TEXT
)
""")
# Insert data
cursor.execute("INSERT OR IGNORE INTO Students VALUES(1,'Pratik')")
cursor.execute("INSERT OR IGNORE INTO Students VALUES(2,'Rahul')")
cursor.execute("INSERT OR IGNORE INTO Courses VALUES(101,1,'Python')")
cursor.execute("INSERT OR IGNORE INTO Courses VALUES(102,2,'Data Science')")
conn.commit()
#INNER JOIN
query = """SELECT Students.Name, Courses.Course_Name FROM Students INNER JOIN Courses ON Students.Student_ID = Courses.Student_ID"""
cursor.execute(query)
print("Students Course Details")
for row in cursor.fetchall():
  print(row)
conn.close()