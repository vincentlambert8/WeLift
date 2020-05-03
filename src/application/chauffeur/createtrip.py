from flask import render_template, request, Blueprint, redirect, session
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
trip = Blueprint('trip', __name__, template_folder=templates_dir)

@trip.route('/createtrip', methods=(['POST']))
def createtrip():

    print('createtrip')

    conn = get_db()
    cur = conn.cursor()

    departure = request.form['departure']
    destination = request.form['destination']
    date = request.form['date']
    distance = request.form['distance']
    capacity = request.form['capacity']
    stopover = request.form['stopover']
    price = request.form['price']
    #id = id du user de la session


    command = "INSERT INTO trips VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}', NULL, NULL, {});".format(date, departure, destination, distance, capacity, stopover, price)
    cur.execute(command)
    conn.commit()
    #session['user_id'] = 
    cur.close()
    conn.close()
    return redirect('choosecar')


