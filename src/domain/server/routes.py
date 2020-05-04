from flask import render_template, request, Blueprint, redirect, session, url_for
import os
import pymysql, pymysql.cursors
import yaml
from .connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
router = Blueprint('router', __name__, template_folder=templates_dir)


@router.route('/home')
@router.route('/')
def home():
    return render_template('home.html')


@router.route('/login')
def login():
    return render_template('login.html')

@router.route('/register')
def register():
    return render_template('/register.html')

#------------------------------------------------------------------------------------------------------------

@router.route('/index')
def index():
    if(session.get('ID', None) is not None):
        conn = get_db()
        cur = conn.cursor()
        command = "SELECT first_name FROM users where id = '{}'".format(session["ID"])
        cur.execute(command)
        bienvenue = cur.fetchone()[0]
        return render_template("index.html", bienvenue=bienvenue)
    else:
        return redirect('home')

@router.route('/users')
def users():
    if(session.get('ID', None) is not None):
        return render_template('users.html')
    else:
        return redirect('home')


#------------------------------------------------------------------------------------------------------------

@router.route('/searchlift')
def searchlift():
    if(session.get('ID', None) is not None):
        return render_template('searchlift.html')
    else:
        return redirect('home')

        
@router.route('/paymentTrip')
def payment():
    if(session.get('ID', None) is not None):
        return render_template('paymentTrip.html')
    else:
        return redirect('home')

#------------------------------------------------------------------------------------------------------------

@router.route('/createtrip', methods=(['GET']))
def createtrip():
    if(session.get('ID', None) is not None):
        return render_template('createtrip.html')
    else:
        return redirect('home')


@router.route('/choosecar')
def choosecar():
    if(session.get('ID', None) is not None):
        return render_template('choosecar.html')
    else:
        return redirect('home')


@router.route('/confirmtrip')
def confirmtrip():
    if(session.get('ID', None) is not None):
        return render_template('confirmtrip.html')
    else:
        return redirect('home')


#-------------------------------------------------------------------------------------------------------------

@router.route('/pickupinfo')
def pickupinfo():
    if(session.get('ID', None) is not None):
        return render_template('pickupinfo.html')
    else:
        return redirect('home')


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

