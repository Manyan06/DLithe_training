import sqlite3
conn = sqlite3.connect("store.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    stock INTEGER
       )
    """)
cursor.execute("INSERT OR IGNORE INTO products VALUES(101, 'Laptop',20)")
try:
  quantity = 2
  cursor.execute("""
  UPDATE products
  SET stock = stock-? WHERE product_id = 101
  """, (quantity,))
  
  cursor.execute("""
  UPDATE products
  SET stock = stock + 1
  WHERE product_id = 101
  """)
  conn.commit()
except Exception:
  print("Purchase Failed!")
  conn.rollback()
  print("Rollback Completed")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
  print(row)
conn.close()