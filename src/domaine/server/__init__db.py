from flask import Flask
from flask_mysqldb import MySQL
import yaml


def get_db(app):
    
    db = yaml.load(open('db.yaml'))

    app.config['MYSQL_HOST'] = db['mysql_host']
    app.config['MYSQL_USER'] = db['mysql_user']
    app.config['MYSQL_PASSWORD'] = db['mysql_password']
    app.config['MYSQL_DB'] = db['mysql_db']

    mysql = MySQL(app)
    return mysql
   

    
  