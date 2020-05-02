from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import get_db from __init__db.py 
 
if __name__ == '__main__':
    app = Flask(__name__)
    sql = get_db(app)
    cur = mysql.connection.cursor()
    a = cur.execute("Select * from cars")
    print(sql.cursor)
    app.run(debug=True)