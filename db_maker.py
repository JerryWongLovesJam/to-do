import sqlite3

print("wa's goodie its workin")
# tells us if the program is working or not until we see ()
conn = sqlite3.connect('todo.db')
# python will create a file called 'todo.db'
conn.execute("CREATE TABLE todo (category VARCHAR(50), item VARCHAR(100), id INTEGER PRIMARY KEY)")

conn.execute("INSERT INTO todo(category, item) VALUES ('Shopping', 'eggs')")
# likewise, (x,y) -> (x,y) in the explanation; 'shopping' as a category and 'eggs' as an item.
conn.execute("INSERT INTO todo(category, item) VALUES ('Shopping', 'milk')")
conn.execute("INSERT INTO todo(category, item) VALUES ('Shopping', 'flour')")
conn.execute("INSERT INTO todo(category, item) VALUES ('Activity', 'Clean house')")
conn.execute("INSERT INTO todo(category, item) VALUES ('Activity', 'Wash the dishes')")

conn.commit()

print("WE DID IT!!")
