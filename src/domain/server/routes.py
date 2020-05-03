from flask import render_template, request, Blueprint, redirect
import os
import bcrypt

templates_dir = os.path.abspath('../../presentation/templates')
router = Blueprint('router', __name__, template_folder=templates_dir)


@router.route('/logo')
def logo():

        return rende_template("assets/logo2.png", logo_img)


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
            email = request.form['email']
            password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            firstName = request.form['fname']
            lastName = request.form['lname']
            gender = request.form['gender']
            birthday = request.form['birthday']
            country = request.form['country']
            phone = request.form['phone']
            balance = 0.0
            #cur = mysql.connection.cursor()
            #cur.execute("INSERT INTO users \
            #(id, email, password, first_name, last_name, gender, birthdate, country, phone, balance) \
            # VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %f)",\
             # (thwart(email), thwart(password), thwart(firstName), gender, birthday, thwart(country), thwart(phone), balance))
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

