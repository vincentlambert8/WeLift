from flask import render_template

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/register')
def register():
        return render_template('register.html')

#------------------------------------------------------------------------------------------------------------

@app.route('/index')
def index():
        return render_template('index.html')

@app.route('/searchlift')
def searchlift():
        return render_template('searchlift.html')
        
@app.route('/payment')
def payment():
        return render_template('payment.html')

#------------------------------------------------------------------------------------------------------------

@app.route('/createtrip')
def createtrip():
        return render_template('createtrip.html')

@app.route('/choosecar')
def choosecar():
        return render_template('choosecar.html')

@app.route('/confirmtrip')
def confirmtrip():
        return render_template('confirmtrip.html')

#-------------------------------------------------------------------------------------------------------------

@app.route('/pickupinfo')
def pickupinfo():
        return render_template('pickupinfo.html')

@app.route('/review')
def review():
        return render_template('review.html')
        
@app.route('/logout')
def logout():
        return render_template('logout.html')

