from flask import Flask, request, redirect, render_template
from flask_mysqldb import MySQL
from __init__db import get_db
from routes import router
import os

app = Flask(__name__)
app.register_blueprint(router)
 
if __name__ == '__main__':
    mysql = get_db(app)
    app.run(debug=True)