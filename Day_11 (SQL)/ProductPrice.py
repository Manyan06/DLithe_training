import sqlite3
conn = sqlite3.connect('product.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS product(
      pid INTEGER,
      pname TEXT,
      price REAL
      )
""")
cursor.execute("INSERT INTO product VALUES (101, 'Mouse', 350)")
cursor.execute("INSERT INTO product VALUES (102, 'Graphic Card', 3000)")
conn.commit()
new_price = float(input("Enter New Price: "))
conn.execute(
  "UPDATE product SET price=? WHERE pid=101",(new_price,)
)
conn.commit()
cursor.execute("SELECT * FROM product")
print(cursor.fetchone())
conn.close()