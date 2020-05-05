from flask import render_template, request, Blueprint, redirect, session, flash
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
user = Blueprint('user', __name__, template_folder=templates_dir)


@user.route('/users')
def users():
    if(session.get('ID', None) is not None):
        user_id = session.get('ID', None)
        if user_id == None:
            flash("The user is not valid")
            return render_template("users.html")
        else:
            conn = get_db()
            cur = conn.cursor()
            command = "SELECT * FROM users WHERE id = {}".format(user_id)
            cur.execute(command)
            conn.commit()
            user = cur.fetchone()

            commandTripAsDriver = "SELECT * FROM trips WHERE id_driver = {}".format(user_id)
            cur.execute(commandTripAsDriver)
            conn.commit()

            tripAsDriver = cur.fetchall()

            commandTripAsPassenger = "SELECT * FROM trips WHERE id_passengers LIKE %'/{}'%".format(user_id)
            cur.execute(commandTripAsPassenger)
            conn.commit()

            tripAsPassenger = cur.fetchall()
            return render_template('users.html', user=user, tripAsDriver=tripAsDriver, tripAsPassenger=tripAsPassenger)
    else:
        return redirect('home', user=user, )