from flask import Flask, request, redirect, render_template
from flask_mysqldb import MySQL
#from domain.server.__init__db import get_db
from domain.server.routes import router
from application.auth.auth import auth
import os

app = Flask(__name__)
app.register_blueprint(router)
app.register_blueprint(auth)
 
if __name__ == '__main__':
    #mysql = get_db(app)
    app.run(debug=True)
    