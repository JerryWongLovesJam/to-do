import sqlite3
from bottle import route, run

@route('/')
def todo_list():