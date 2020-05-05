from flask import render_template, request, Blueprint, redirect, session, flash
import os
import pymysql, pymysql.cursors
import yaml
import unidecode
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
trip = Blueprint('trip', __name__, template_folder=templates_dir)

@trip.route('/createtrip', methods=(['POST']))
def createtrip():
    conn = get_db()
    cur = conn.cursor()

    departure = unidecode.unidecode(request.form['departure']).lower()
    destination = unidecode.unidecode(request.form['destination']).lower()
    date = request.form['date']
    distance = request.form['distance']

    if(distance == ""):
        distance = None

    print(distance)
    stopover = request.form['stopover']
    price = request.form['price']

    if(price == ""):
        price = 0

    if request.form['stopover'] == "yes":
        stopover = 1
    elif request.form['stopover'] == "no":
        stopover = 0
    elif request.form['stopover'] == "other":
        stopover = 2

    if(validateEmpty(request.form)):
        return render_template('createtrip.html')
    else:
        command = "INSERT INTO trips VALUES (NULL, '{}', '{}', '{}', '{}', NULL, '{}', '{}', NULL, '{}', NULL)".format(date, departure, destination, distance, stopover, session['ID'], price)
        cur.execute(command)
        tripId = conn.insert_id()
        conn.commit()

    cur.close()
    conn.close()
    return redirect("choosecar/{}".format(tripId))


def validateEmpty(form):
    if(form['departure'] == ""):
        flash("Departure can't be empty")
    elif(form['destination'] == ""):
        flash("Destination can't be empty")
    elif(form['date'] == ""):
        flash("Date can't be empty")
    else:
        return False
    return True