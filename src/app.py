from flask import Flask, request, redirect, render_template, session
from domain.server.routes import router
from application.auth.auth import auth
from application.chauffeur.createtrip import trip
from application.chauffeur.choosecar import car
from application.client.searchlift import search
from application.client.payment import chooseTrip
from application.client.fillAccount import fill
from application.both.users import user
from application.chauffeur.confirmtrip import confirmation
from application.both.pickupinfo import pickup
from application.both.reviews import driverReview
import os
import bcrypt

app = Flask(__name__)
app.register_blueprint(router)
app.register_blueprint(auth)
app.register_blueprint(trip)
app.register_blueprint(car)
app.register_blueprint(search)
app.register_blueprint(chooseTrip)
app.register_blueprint(fill)
app.register_blueprint(user)
app.register_blueprint(confirmation)
app.register_blueprint(pickup)
app.register_blueprint(driverReview)

if __name__ == '__main__':
    app.secret_key = "_0123jcyoukvince!"
    app.run(debug=True)
    