from flask import Flask, request, redirect
from flask_mysqldb import MySQL
import get_db from __init__db.py 
 
if __name__ == '__main__':
    app = Flask(__name__)
    mysql = get_db(app)
    app.run(debug=True)