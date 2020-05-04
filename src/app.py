from flask import Flask, request, redirect, render_template, session
from domain.server.routes import router
from application.auth.auth import auth
from application.chauffeur.createtrip import trip
import os
import bcrypt

app = Flask(__name__)
app.register_blueprint(router)
app.register_blueprint(auth)
app.register_blueprint(trip)
 
if __name__ == '__main__':
    app.secret_key = "_0123jcyoukvince!"
    app.run(debug=True)
    