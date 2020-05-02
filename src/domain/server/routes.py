from flask import render_template, Blueprint
import os

templates_dir = os.path.abspath('../../presentation/templates')
router = Blueprint('router', __name__, template_folder=templates_dir)

@router.route('/')
def home():
        return render_template("home.html")

@router.route('/login')
def login():
        return render_template('login.html')

@router.route('/register')
def register():
        return render_template('register.html')

#------------------------------------------------------------------------------------------------------------

@router.route('/index')
def index():
        return render_template('index.html')


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

