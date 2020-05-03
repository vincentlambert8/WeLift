from flask import render_template, request, Blueprint, redirect, session
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
car = Blueprint('car', __name__, template_folder=templates_dir)

@car.route('/choosecar', methods=(['POST']))
def choosecar():

    conn = get_db()
    cur = conn.cursor()

    license = request.form['license']
    brand = request.form['brand']
    model = request.form['model']
    year = request.form['year']
    color = request.form['color']
 


    command = "INSERT INTO cars VALUES ('{}', '{}', '{}', '{}', '{}');".format(license, brand, model, year, color)
    cur.execute(command)
    conn.commit()

    cur.close()
    conn.close()
    return redirect('pickupinfo')
