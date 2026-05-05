"""Creates the todo database"""
import sqlite3
# imports the sqlite library

print("wa's goodie its startin to workin")
print("Stared created the todo database")
# tells us if the program is working or not until we see ("...")

conn = sqlite3.connect('todo.db')
# python will create a file called 'todo.db'

conn.execute("CREATE TABLE todo (category VARCHAR(50), item VARCHAR(100), id INTEGER PRIMARY KEY)")
# Creates the table with 3 fields
# VARCHAR = variable character(s)

conn.execute("INSERT INTO todo(category, item) VALUES ('Shopping', 'Eggs')")
conn.execute("INSERT INTO todo(category, item) VALUES ('Shopping', 'Milk')")
conn.execute("INSERT INTO todo(category, item) VALUES ('Shopping', 'Flour')")
conn.execute("INSERT INTO todo(category, item) VALUES ('Activity', 'Clean house')")
conn.execute("INSERT INTO todo(category, item) VALUES ('Activity', 'Wash the dishes')")

# likewise, (x,y) -> (x,y) in the explanation; 'Shopping' as a category and 'eggs' as an item.
# creates 5 records to the table

conn.commit()
# saves changes

print("it worked")
print("Database has been created.")
# tells us it worked
