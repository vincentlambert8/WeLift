from flask import render_template, request, Blueprint, redirect, session
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
search = Blueprint('search', __name__, template_folder=templates_dir)

@search.route('/searchlift', methods=(['POST']))
def searchlift():
    print("searCH")

    conn = get_db()
    cur = conn.cursor()

    if request.form['departure'] != "":
        departure = request.form['departure']
        departureQuery = " T.departure LIKE '%{}%' AND".format(departure)
    else:
        departureQuery = ""


    if request.form['destination'] != "":
        destination = request.form['destination']
        destinationQuery = " T.destination LIKE '%{}%' AND".format(destination)
    else:
        destinationQuery = ""


    if request.form['date'] != "":
        date = request.form['date']
        dateQuery = " T.date LIKE %'{}'% AND".format(date)
    else:
        dateQuery = ""


    if request.form['numberOfPassengers'] != "":
        numberOfPassengers = request.form['numberOfPassengers']
        numberOfPassengersQuery = " T.capacity >= '{}' AND".format(numberOfPassengers)
    else: 
        numberOfPassengers = 1
        numberOfPassengersQuery = " T.capacity >= 1 AND"


    if request.form['maxPrice'] != "":
        maxPrice = request.form['maxPrice']
        maxPriceQuery = " T.Price <= '{}'".format(maxPrice)
    else: 
        maxPriceQuery = " T.Price > 0"

    
    command = "SELECT * FROM trips T WHERE" + departureQuery + destinationQuery + dateQuery + numberOfPassengersQuery + maxPriceQuery
    cur.execute(command)
    print(command)

    trajets = cur.fetchall()
 
    cur.close()
    conn.close()
    return render_template("searchlift.html",trajets=trajets)




 