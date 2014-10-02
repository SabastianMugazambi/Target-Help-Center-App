import os
from sqlite3 import dbapi2
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Markup
from contextlib import closing
import twilio.twiml
from twilio.rest import TwilioRestClient
from pprint import pprint
from send_sms import sms
import random


DATABASE = 'thing.db'
DEBUG = True
SECRET_KEY = 'jjjgl'

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode = 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def connect_db():
    return dbapi2.connect(app.config['DATABASE'])
 
@app.before_request
def before_request():
    g.db = connect_db()
 
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/monitor')
def show_wimpers():
    cur = get_db().execute('select * from wimpers order by id desc')
    stuff  = cur.fetchall()
    cur.close()
    return render_template('show_wimpers.html', W = stuff)

@app.route("/", methods=['GET', 'POST'])
def add_wimper(): #ADD THE HELP OPTION
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    msg = str(request.values['Body'])
    l = msg.split("#")
    aile = l[0]
    xname = l[1]
    xmessage = l[2]

    e_number = random.randint(0,13)
    employee = ["billy","Sam","Anna","Chet","Taylor","Saba","Sam","Nik","Joe","Samantha","Robert","Bob","Kenn","David"]
    xemployee = employee[e_number]
    xstatus = "waiting"
    mid = ". An agent will be with you in a moment! You said "
    sms()
    resp.message("Hello " + xname + mid + xmessage)
    g.db.execute('insert into wimpers (num, name, message, employee, status) values (?,?,?,?,?)', [aile, xname, xmessage, xemployee, xstatus])
    g.db.commit()
    return str(resp)
#@app.route("http://api.target.com/v2/products/storeLocations?productId=070-09-0141&storeId=694&key=[J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF]")
#def check_product ():
    #return 

if __name__ == '__main__':
    app.run(debug=True)
