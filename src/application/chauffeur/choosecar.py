from flask import render_template, request, Blueprint, redirect, session, url_for
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
car = Blueprint('car', __name__, template_folder=templates_dir)

@car.route('/choosecar/<id>', methods=(['POST']))
def choosecar(id):
    conn = get_db()
    cur = conn.cursor()

    license = request.form['license']
    brand = request.form['brand']
    model = request.form['model']
    capacity = request.form['capacity']
    year = request.form['year']
    color = request.form['color']

    command = "INSERT INTO cars VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(license, brand, model, capacity, year, color)
    cur.execute(command)

    command = "UPDATE trips T SET T.license = '{}', T.seats_available = '{}' WHERE T.id = '{}'".format(license, capacity, id)
    cur.execute(command)

    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('pickupinfo'))
