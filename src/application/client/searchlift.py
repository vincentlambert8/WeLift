from flask import render_template, request, Blueprint, redirect, session
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
search = Blueprint('search', __name__, template_folder=templates_dir)

@search.route('/searchlift', methods=['GET', 'POST'])
def searchlift():
    if(session.get('ID', None) is not None):
        conn = get_db()
        cur = conn.cursor()

        if(request.method == 'POST'):
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


            if request.form['seats'] != "":
                numberOfPassengers = request.form['seats']
                numberOfPassengersQuery = " T.seats_available >= '{}' AND".format(numberOfPassengers)
            else:
                numberOfPassengers = 1
                numberOfPassengersQuery = " T.seats_available >= 1 AND"


            if request.form['maxPrice'] != "":
                maxPrice = request.form['maxPrice']
                maxPriceQuery = " T.Price <= '{}'".format(maxPrice)
            else:
                maxPriceQuery = " T.Price > 0"


            command = "SELECT * FROM trips T WHERE" + departureQuery + destinationQuery + dateQuery + numberOfPassengersQuery + maxPriceQuery + " AND date > NOW() ORDER BY date"
            cur.execute(command)
            trajets = cur.fetchall()

        else:
            command = "SELECT * FROM trips WHERE seats_available != 0 AND date > NOW() ORDER BY date"
            cur.execute(command)
            trajets = cur.fetchall()

        cur.close()
        conn.close()
        return render_template("searchlift.html",trajets=trajets)

    else:
        return redirect('../home')


 