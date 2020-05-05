from flask import render_template, request, Blueprint, redirect, session, url_for
import os
import pymysql, pymysql.cursors
import yaml
from .connection_db import get_db
from datetime import datetime

templates_dir = os.path.abspath('presentation/templates')
router = Blueprint('router', __name__, template_folder=templates_dir)


@router.route('/home')
@router.route('/')
def home():
    conn = get_db()
    cur = conn.cursor()
    command = "SELECT * FROM trips WHERE seats_available != 0 AND date > NOW() ORDER BY date"
    cur.execute(command)
    trips = cur.fetchall()

    return render_template('home.html', trips=trips[:18])


@router.route('/login')
def login():
    return render_template('login.html')

@router.route('/register')
def register():
    return render_template('/register.html')

#------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------------------------------

@router.route('/searchlift')
def searchlift():
    if(session.get('ID', None) is not None):
        return render_template('searchlift.html')
    else:
        return redirect('home')



#------------------------------------------------------------------------------------------------------------

@router.route('/createtrip', methods=(['GET']))
def createtrip():
    if(session.get('ID', None) is not None):
        return render_template('createtrip.html')
    else:
        return redirect('home')


@router.route('/choosecar/<int:id>')
def choosecar(id):
    if(session.get('ID', None) is not None):
        conn = get_db()
        cur = conn.cursor()

        commandGetDriverId = "SELECT id_driver FROM trips WHERE id = {}".format(id)
        cur.execute(commandGetDriverId)
        id_driver = cur.fetchone()[0]

        commandGetCarForThisDriver = "SELECT * FROM cars WHERE id_driver = {}".format(id_driver)
        cur.execute(commandGetCarForThisDriver)
        userCars = cur.fetchall()

        cur.close()
        conn.close()
        return render_template('choosecar.html', id=id, id_driver=id_driver, userCars=userCars)
    else:
        return redirect('home')


#-------------------------------------------------------------------------------------------------------------

@router.route('/review')
def review():
    if(session.get('ID', None) is not None):
        return render_template('review.html')
    else:
        return redirect('home')


@router.route('/logout')
def logout():
    session.pop('ID', None)
    return render_template('logout.html')

