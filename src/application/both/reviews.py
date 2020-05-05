from flask import render_template, request, Blueprint, redirect, session, flash
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
driverReview = Blueprint('driverReview', __name__, template_folder=templates_dir)

@driverReview.route('/review/<id>', methods=['GET', 'POST'])
def review(id):
    userId = session.get('ID', None)
    if(session.get('ID', None) is not None):
        conn = get_db()
        cur = conn.cursor()

        commandGetTrip = "SELECT * FROM Trips WHERE id = {}".format(id)
        cur.execute(commandGetTrip)
        currentTrip = cur.fetchone()

        if(request.method == 'POST'):
            rating = request.form['rating']
            message = request.form['message']

            commandInsertComments = "INSERT INTO Comments VALUES (NULL, '{}', '{}', '{}', '{}')".format(message, rating, userId, currentTrip[7])
            cur.execute(commandInsertComments)
            conn.commit()

            cur.close()
            conn.close()
            flash("Your review was submit")
            return redirect('../users')

        else:
            cur.close()
            conn.close()
            return render_template('review.html', trip = currentTrip)
    else:
        return redirect('../home')


