"""Creates a webserver for interacting with the todo database."""
# Imports required modules
import sqlite3
from bottle import route, run, request, redirect

def execute_query(query, params=(), fetch=False):
    """Handles database queries and interactions."""
    # Connects to the database
    with sqlite3.connect('todo.db') as conn:
        # Executes SQL queru and returns result
        cur = conn.execute(query, params)
        return cur.fetchall() if fetch else None

@route('/')
def todo_list():
    """Set path to the home page"""
    rows = execute_query("SELECT id, category, item FROM todo ORDER BY category, item", fetch=True)

    table_rows = ""
    for row in rows:
        row_id, category, item = row

        table_rows += f"""
        <tr>   
            <td>{category}</td>
            <td>{item}</td>
            <td>    
                <form action='/delete' method='POST'>
                    <input type='hidden' name=delitem value='{row_id}'>
                    <button type='submit'>Delete</button>
                </form>
            </td>
        </tr>
        """

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>To-do list</title>
        </head>
        <body>
            <h1>To-do list</h1>
            <form action="/new", method="POST">
                <input type="text" name="newcat" placeholder="Category" required>
                <input type="text" name="item" placeholder="New item" required>
                <button tpe="submit">Add</button>
            </form>
            <table>
                <tr>
                    <th>Category</th>
                    <th>Item</th>
                    <th>Action</th>
                </tr>
                {table_rows}
            </table>
        </body>
        </html>
        """

    return html

@route('/delete', method="POST")
def delete_item():
    delid = request.forms.get("delitem")
    if delid:
        execute_query("DELETE FROM todo WHERE id = ?", (delid,))
    redirect('/')

# Starts the webserver
run(host = 'localhost', port = 8080)
