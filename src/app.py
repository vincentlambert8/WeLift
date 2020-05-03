from flask import Flask, request, redirect, render_template, session
from domain.server.routes import router
from application.auth.auth import auth
import os
import bcrypt

app = Flask(__name__)
app.register_blueprint(router)
app.register_blueprint(auth)
 
if __name__ == '__main__':
    app.secret_key = "0123jcyoukvince!"
    app.run(debug=True)
    