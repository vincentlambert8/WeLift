from flask import render_template, request, Blueprint, redirect, session, url_for
import os
import pymysql, pymysql.cursors
import yaml
from .connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
router = Blueprint('router', __name__, template_folder=templates_dir)


@router.route('/logo')
def logo():
    return render_template("assets/logo2.png", logo_img)

@router.route('/home')
@router.route('/')
def home():
    conn = get_db()
    cur = conn.cursor()
    if(session.get("ID", None) is not None):
        command = "SELECT first_name FROM users where id = '{}'".format(session["ID"])
        cur.execute(command)
        firstName = cur.fetchone()[0]
        return render_template("home.html", firstName=firstName)
    else:
        return render_template("home.html", firstName="Tu n'est pas connecté")


@router.route('/login')
def login():
    return render_template('login.html')

@router.route('/register', methods=(['GET']))
def register():
    return render_template('/register.html')

#------------------------------------------------------------------------------------------------------------

@router.route('/index')
def index():
    return render_template('index.html')

@router.route('/users')
def users():
    return render_template('users.html')


#------------------------------------------------------------------------------------------------------------

@router.route('/searchlift')
def searchlift():
    return render_template('searchlift.html')
        
@router.route('/payment')
def payment():
    return render_template('payment.html')

#------------------------------------------------------------------------------------------------------------

@router.route('/createtrip')
def createtrip():
    return render_template('createtrip.html')

@router.route('/choosecar')
def choosecar():
    return render_template('choosecar.html')

@router.route('/confirmtrip')
def confirmtrip():
    return render_template('confirmtrip.html')

#-------------------------------------------------------------------------------------------------------------

@router.route('/pickupinfo')
def pickupinfo():
    return render_template('pickupinfo.html')

@router.route('/review')
def review():
    return render_template('review.html')

@router.route('/logout')
def logout():
    session.pop('ID', None)
    return render_template('logout.html')

