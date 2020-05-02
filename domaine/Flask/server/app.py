from flask import Flask, request, redirect
from flask_mysqldb import MySQL
from __init__db import get_db



app = Flask(__name__)

@app.route('/')
def index():
        return 'HELLLO'


 
if __name__ == '__main__':

    mysql = get_db(app)
    app.run(debug=True)