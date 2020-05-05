from flask import render_template, request, Blueprint, redirect, session
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
chooseTrip = Blueprint('chooseTrip', __name__, template_folder=templates_dir)


@chooseTrip.route('/paymentTrip/<id>')
def payment(id):
    if(session.get('ID', None) is not None):
        conn = get_db()
        cur = conn.cursor()
        commandTrip = "SELECT * FROM Trips WHERE id = {}".format(id)

        cur.execute(commandTrip)
        currentTrip = cur.fetchone()

        commandDriverReviews = "SELECT * FROM comments WHERE id_driver = {}".format(currentTrip[7])

        cur.execute(commandDriverReviews)
        reviews = cur.fetchall()

        commandDriverName = "SELECT first_name, last_name FROM users WHERE id = {}".format(currentTrip[7])

        cur.execute(commandDriverName)
        driver = cur.fetchone()

        commandCar = "SELECT * FROM Cars WHERE license = '{}'".format(currentTrip[10])

        cur.execute(commandCar)
        car = cur.fetchone()


        return render_template('paymentTrip.html', currentTrip=currentTrip, reviews=reviews, driver=driver, car=car)
    else:
        return redirect('home')