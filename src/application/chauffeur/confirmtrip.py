from flask import render_template, request, Blueprint, redirect, session, flash
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
confirmation = Blueprint('confirmation', __name__, template_folder=templates_dir)

@confirmation.route('/confirmtrip/<id>')
def confirmtrip(id):
    userId = session.get('ID', None)
    if(userId is not None):
        conn = get_db()
        cur = conn.cursor()

        commandGetTrip = "SELECT * FROM Trips WHERE id = {}".format(id)
        cur.execute(commandGetTrip)
        currentTrip = cur.fetchone()

        if(currentTrip[5] == 0):
            cur.close()
            conn.close()
            return redirect('../home')

        else:
            commandGetUserBalance = "SELECT balance FROM Users WHERE id = '{}'".format(userId)
            cur.execute(commandGetUserBalance)
            userBalance = cur.fetchone()
            newUserBalance = userBalance[0] - currentTrip[9]

            if(newUserBalance < 0):
                cur.close()
                conn.close()
                return redirect('../home')

            else:
                commandSetUserBalance = "UPDATE users U SET U.balance = '{}' WHERE id = '{}'".format(newUserBalance, userId)
                cur.execute(commandSetUserBalance)
                conn.commit()

                commandGetDriverBalance = "SELECT balance FROM Users WHERE id = '{}'".format(currentTrip[7])
                cur.execute(commandGetDriverBalance)
                driverBalance = cur.fetchone()
                newDriverBalance = currentTrip[9] + driverBalance[0]
                commandSetDriverBalance = "UPDATE users U SET U.balance = '{}' WHERE id = '{}'".format(newDriverBalance, currentTrip[7])
                cur.execute(commandSetDriverBalance)
                conn.commit()

                updatedSeats = currentTrip[5] - 1
                if(currentTrip[8] == None):
                    newPassenger = "/" + str(userId)
                else:
                    newPassenger = currentTrip[8] + "/" + str(userId)
                commandSetTrip = "UPDATE trips T SET T.seats_available = '{}', T.id_passengers = '{}' WHERE T.id = '{}'".format(updatedSeats, newPassenger, id)
                cur.execute(commandSetTrip)
                conn.commit()

                commandGetDriver = "SELECT * FROM Users WHERE id = '{}'".format(currentTrip[7])
                cur.execute(commandGetDriver)
                driver = cur.fetchone()

        cur.close()
        conn.close()
        return render_template('confirmtrip.html', driver=driver, userBalance=newUserBalance)
    else:
        return redirect('../home')