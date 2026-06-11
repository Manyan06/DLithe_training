import sqlite3
conn = sqlite3.connect('book.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
      book_id INTEGER,
      title TEXT
      )
""")
cursor.execute("INSERT INTO books VALUES (1, 'Python')")
cursor.execute("INSERT INTO books VALUES (2, 'SQL Basics')")
cursor.execute("INSERT INTO books VALUES (3, 'Data Science')")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM books")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM books")
count = cursor.fetchone()[0]
print("Total Books: ", count)
conn.close()