from flask import render_template, request, Blueprint, redirect
import os
import bcrypt
import pymysql, pymysql.cursors
import yaml

templates_dir = os.path.abspath('../../presentation/templates')
auth = Blueprint('auth', __name__, template_folder=templates_dir)


@auth.route('/register', methods=(['POST']))
def register_auth():
        db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
        conn = pymysql.connect(host=db_config['mysql_host'], user=db_config['mysql_user'], password=db_config['mysql_password'], db=db_config['mysql_db'])
        cur = conn.cursor()

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
            validation = "SELECT * FROM users WHERE email = '{}'".format(email)
            responseValidation = cur.execute(validation)
            if responseValidation > 0:
                print("This email is already use")
                return render_template('register.html')
            else:
                command = "INSERT INTO Users VALUES (NULL, '{}', MD5('{}'), '{}', '{}', '{}', '{}', '{}', '{}', {});".format(email, password, firstName, lastName, gender, birthday, country, phone, balance)
                cur.execute(command)
                conn.commit()
        except Exception as e:
            print(e)

        cur.close()
        conn.close()
        return redirect('login')