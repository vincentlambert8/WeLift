from flask import render_template, request, Blueprint, redirect, session, flash
import os
import pymysql, pymysql.cursors
import yaml
from domain.server.connection_db import get_db
from datetime import date

templates_dir = os.path.abspath('presentation/templates')
fill = Blueprint('fill', __name__, template_folder=templates_dir)


@fill.route('/fillAccount/<id>', methods=['GET', 'POST'])
def fillAccount(id):
    if(session.get('ID', None) is not None):
        userId = session.get('ID', None)
        conn = get_db()
        cur = conn.cursor()

        commandUserMoney = "SELECT balance FROM users WHERE id = {}".format(id)
        cur.execute(commandUserMoney)
        amount = cur.fetchone()
        if(request.method == 'GET'):
            cur.close()
            conn.close()
            return render_template('fillAccount.html', amount=amount[0], id=id)
        else:
            moneyDeposit = request.form['amount']
            if(moneyDeposit == ""):
                moneyDeposit = 0
            elif(float(moneyDeposit) < 0.0):
                flash("You can't add negative amount.")
                cur.close()
                conn.close()
                return render_template('fillAccount.html', amount=amount[0], id=id)

            amountTotal = float(amount[0]) + float(moneyDeposit)
            commandUpdateMoney = "UPDATE users U SET U.balance = '{}' WHERE U.id = '{}'".format(amountTotal, id)
            cur.execute(commandUpdateMoney)
            conn.commit()

            commandWriteTransaction = "INSERT INTO Transactions VALUES (NULL, '{}', '{}', '{}', '{}')".format(userId, userId, moneyDeposit, date.today())
            cur.execute(commandWriteTransaction)
            conn.commit()

            cur.close()
            conn.close()
            return render_template('fillAccount.html', amount=amountTotal, id=id)
    else:
        return redirect('home')

