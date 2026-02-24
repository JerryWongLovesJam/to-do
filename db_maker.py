import sqlite3

print("wa's goodie")

conn = sqlite3.connect('todo.db')

conn.execute("CREATE TABLE todo(catergory VARCHAR(50), item VARCHAR(100), id INTEGER PRIMARY KEY)")

