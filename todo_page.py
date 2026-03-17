import sqlite3
from bottle import route, run

def execute_query():

@route('/')
def todo_list():
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM todo")
    result = cur.fetchall()
    cur.close()

    return str(result)

run(host = 'localhost', port = 8080)
