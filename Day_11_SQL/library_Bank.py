import sqlite3
conn = sqlite3.connect("digital_library.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS library_stocks(
      id INTEGER PRIMARY KEY,
      book_name TEXT,
      total_books INTEGER,
      borrowed_books INTEGER
      )
""")
cursor.execute("INSERT INTO library_stocks VALUES " "(1, 'Data Scienec Handbook', 15, 0)""")
try:
  issue_count = 1
  cursor.execute("""
  UPDATE library_stocks
  SET total_books = total_books - ?
  WHERE id = 1 
  """, (issue_count,))
  
  cursor.execute("""
  UPDATE library_stocks
  SET borrowed_books = borrowed_books + ? WHERE id = 1 
  """, (issue_count,))
  conn.commit()
  print("Book Issued Successfully")
  print("Transaction Committed")

except Exception as e:
  conn.rollback()
  print("Transaction Failed")
  print(e)

print("/n Library Status")
print("-" * 40)
cursor.execute("SELECT * FROM library_stocks")
for row in cursor.fetchall():
    print(row)
conn.close()