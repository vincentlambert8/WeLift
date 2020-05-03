from flask import render_template, request, Blueprint, redirect
import os
import bcrypt
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db

templates_dir = os.path.abspath('presentation/templates')
auth = Blueprint('auth', __name__, template_folder=templates_dir)

@auth.route('/register', methods=(['POST']))
def register_auth():
        conn = get_db()
        cur = conn.cursor()

        auth = False
        email = request.form['email']
        password = request.form['password']
        firstName = request.form['fname']
        lastName = request.form['lname']
        gender = request.form['gender']
        birthday = request.form['birthday']
        country = request.form['country']
        phone = request.form['phone']
        balance = 0.0

        try:
            validation = "SELECT U.email FROM users U WHERE U.email = '{}'".format(email)
            responseValidation = cur.execute(validation)
            if responseValidation > 0:
                print("This email is already use")

            else:
                command = "INSERT INTO Users VALUES (NULL, '{}', MD5('{}'), '{}', '{}', '{}', '{}', '{}', '{}', {});".format(email, password, firstName, lastName, gender, birthday, country, phone, balance)
                cur.execute(command)
                conn.commit()
                auth = True

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        if(auth == True):
            return redirect('home')
        else:
            return render_template('register.html')


@auth.route('/login', methods=(['POST']))
def login_auth():
    conn = get_db()
    cur = conn.cursor()

    auth = False
    email = request.form['email']
    password = request.form['password']

    try:
        userLoginValidation = "SELECT * FROM users U WHERE U.email = '{}' AND U.password = MD5('{}')".format(email, password)
        responseLoginValidation = cur.execute(userLoginValidation)
        if responseLoginValidation == 0:
            print("This account doesn't exist")
        else:
            auth = True

    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()

    if(auth == True):
        return redirect('home')
    else:
        return render_template('login.html')