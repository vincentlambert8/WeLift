from flask import render_template, request, Blueprint, redirect, session, flash
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db
from datetime import date

templates_dir = os.path.abspath('presentation/templates')
confirmation = Blueprint('confirmation', __name__, template_folder=templates_dir)

@confirmation.route('/confirmtrip/<id>', methods=['GET', 'POST'])
def confirmtrip(id):
    userId = session.get('ID', None)
    if(userId is not None):
        conn = get_db()
        cur = conn.cursor()
        newUserBalance = None

        commandGetTrip = "SELECT * FROM Trips WHERE id = {}".format(id)
        cur.execute(commandGetTrip)
        currentTrip = cur.fetchone()

        if(request.method == 'POST'):
            if(currentTrip[5] == 0):
                flash("An error occured")
                cur.close()
                conn.close()
                return redirect('../home')

            else:
                 commandGetUserBalance = "SELECT balance FROM Users WHERE id = '{}'".format(userId)
                 cur.execute(commandGetUserBalance)
                 userBalance = cur.fetchone()
                 newUserBalance = userBalance[0] - currentTrip[9]

                 if(newUserBalance < 0):
                    flash("Please add some fund to your account")
                    cur.close()
                    conn.close()
                    return redirect('../paymentTrip/{}'.format(id))

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

                    commandWriteTransaction = "INSERT INTO Transactions VALUES (NULL, '{}', '{}', '{}', '{}')".format(userId, currentTrip[7], currentTrip[9], date.today())
                    cur.execute(commandWriteTransaction)
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

        commandGetUpdatedTrip = "SELECT * FROM Trips WHERE id = {}".format(id)
        cur.execute(commandGetUpdatedTrip)
        updatedTrip = cur.fetchone()

        licensePlate = updatedTrip[10]
        commandGetCar = "SELECT * FROM Cars WHERE license = '{}'".format(licensePlate)
        cur.execute(commandGetCar)
        car = cur.fetchone()

        cur.close()
        conn.close()
        return render_template('confirmtrip.html', driver=driver, userBalance=newUserBalance, currentTrip=updatedTrip, car=car)
    else:
        return redirect('../home')