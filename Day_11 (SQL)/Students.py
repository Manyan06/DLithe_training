import sqlite3
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
      id INTEGER,
      name TEXT,
      marks INTEGER
      )
""")
cursor.execute("INSERT INTO student VALUES (1, 'Amit', 85)")
cursor.execute("INSERT INTO student VALUES (2, 'Neha', 90)")
conn.commit()
sid = int(input("Enter Student ID: "))
cursor.execute("SELECT * FROM student WHERE id=?",(sid,))
record = cursor.fetchone()
if record:
  print("Student Found: ",record)
else:
  print("Student Not Found")
conn.close()