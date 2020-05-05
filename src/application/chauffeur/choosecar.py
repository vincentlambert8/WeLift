from flask import render_template, request, Blueprint, redirect, session, url_for, flash
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
car = Blueprint('car', __name__, template_folder=templates_dir)

@car.route('/choosecar/<id>/<driverId>', methods=(['POST']))
def choosecar(id, driverId):
    conn = get_db()
    cur = conn.cursor()

    license = request.form['license']
    brand = request.form['brand']
    model = request.form['model']
    capacity = request.form['capacity']
    year = request.form['year']
    color = request.form['color']
    commandCheckIfCarExist = "SELECT license FROM cars WHERE license = '{}'".format(license)
    cars = cur.execute(commandCheckIfCarExist)

    if(cars > 0):
        flash("This car already exist")
        cur.close()
        conn.close()
        return redirect("../../choosecar/{}".format(id))
    commandSetCar = "INSERT INTO cars VALUES ('{}', {}, '{}', '{}', '{}', '{}', '{}');".format(license, driverId, brand, model, capacity, year, color)
    cur.execute(commandSetCar)
    conn.commit()

    commandSetTrip = "UPDATE trips T SET T.license = '{}', T.seats_available = '{}' WHERE T.id = '{}'".format(license, capacity, id)
    cur.execute(commandSetTrip)
    conn.commit()

    cur.close()
    conn.close()
    return redirect("../../pickupinfo/{}".format(id))


@car.route('/choosecar/<int:id>/<int:driverId>/<license>', methods=(['POST']))
def chooseExistingCar(id, driverId, license):
    conn = get_db()
    cur = conn.cursor()

    commandGetCapacity = "SELECT capacity FROM cars WHERE license = '{}'".format(license)
    cur.execute(commandGetCapacity)
    capacity = cur.fetchone()[0]

    commandSetTrip = "UPDATE trips T SET T.license = '{}', T.seats_available = '{}' WHERE T.id = '{}'".format(license, capacity, id)
    cur.execute(commandSetTrip)
    conn.commit()

    cur.close()
    conn.close()
    return redirect("../../../pickupinfo/{}".format(id))