from flask import render_template, request, Blueprint, redirect
import os
import bcrypt
import pymysql, pymysql.cursors
import yaml

templates_dir = os.path.abspath('../../presentation/templates')
router = Blueprint('router', __name__, template_folder=templates_dir)


@router.route('/logo')
def logo():
        return render_template("assets/logo2.png", logo_img)


@router.route('/home')
@router.route('/')
def home():
        return render_template("home.html")

@router.route('/login')
def login():
        return render_template('login.html')

@router.route('/register', methods=('GET', 'POST'))
def register():
        if request.method == 'GET':
            return render_template('register.html')
        else:
            db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
            conn = pymysql.connect(host=db_config['mysql_host'], user=db_config['mysql_user'], password=db_config['mysql_password'], db=db_config['mysql_db'])
            cur = conn.cursor()

            email = request.form['email']
            #password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            password = request.form['password']
            firstName = request.form['fname']
            lastName = request.form['lname']
            gender = request.form['gender']
            birthday = request.form['birthday']
            country = request.form['country']
            phone = request.form['phone']
            balance = 0.0

            try:
                command = "INSERT INTO Users VALUES (NULL, '{}', MD5('{}'), '{}', '{}', '{}', '{}', '{}', '{}', {});".format(email, password, firstName, lastName, gender, birthday, country, phone, balance)
                cur.execute(command)
                conn.commit()
            except Exception as e:
                print(e)

            cur.close()
            conn.close()
            return redirect('login')

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
        return render_template('logout.html')

