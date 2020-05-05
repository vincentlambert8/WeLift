from flask import render_template, request, Blueprint, redirect, session, url_for
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
pickup = Blueprint('pickup', __name__, template_folder=templates_dir)

@pickup.route('/pickupinfo/<id>')
def pickupinfo(id):
    if(session.get('ID', None) is not None):
        conn = get_db()
        cur = conn.cursor()

        commandTrip = "SELECT * FROM Trips WHERE id = {}".format(id)
        cur.execute(commandTrip)
        currentTrip = cur.fetchone()

        currentCarLicense = currentTrip[10]
        if(currentCarLicense == None):
            redirect('../choosecar/{}'.format(id))
        else:
            commandGetCar = "SELECT * FROM Cars WHERE license = '{}'".format(currentCarLicense)
            cur.execute(commandGetCar)
            car = cur.fetchone()

            tripPassengers = currentTrip[8]
            passengers = []
            if(tripPassengers != None):
                passengersIdList = tripPassengers.split('/')
                passengersIdList.pop(0)
                if(len(passengersIdList) > 0):
                    for i in range(0, (len(passengersIdList))):
                        commandGetPassenger = "SELECT * FROM Users WHERE id = {}".format(passengersIdList[i])
                        cur.execute(commandGetPassenger)
                        currentPassenger = cur.fetchone()
                        passengers.append(currentPassenger)

        return render_template('pickupinfo.html', currentTrip=currentTrip, car=car, passengers=passengers)
    else:
        return redirect('../home')