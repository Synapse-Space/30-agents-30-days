"""
Creates a sample SQLite database.
"""

import sqlite3


connection = sqlite3.connect("sample.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

id INTEGER PRIMARY KEY,

name TEXT,

email TEXT,

created_at TEXT

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(

id INTEGER PRIMARY KEY,

name TEXT,

price REAL

)
""")

cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM products")

users = [

("Alice","alice@test.com","2026-01-01"),

("Bob","bob@test.com","2026-02-10"),

("Charlie","charlie@test.com","2026-03-15"),

]

products = [

("Laptop",1200),

("Mouse",40),

("Keyboard",70),

]

cursor.executemany(

"""
INSERT INTO users(name,email,created_at)

VALUES(?,?,?)

""",

users,

)

cursor.executemany(

"""
INSERT INTO products(name,price)

VALUES(?,?)

""",

products,

)

connection.commit()

connection.close()

print("Sample database created.")