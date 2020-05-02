from flask import Flask, request, redirect, render_template
from flask_mysqldb import MySQL
from __init__db import get_db
import os

templates_dir = os.path.abspath('../../presentation/templates')
app = Flask(__name__, template_folder=templates_dir)

@app.route('/')
def index():
        return render_template("home.html")

 
if __name__ == '__main__':
    mysql = get_db(app)
    app.run(debug=True)