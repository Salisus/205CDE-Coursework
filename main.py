from flask import Flask
from flask import render_template, render_template_string
from flask import request
import sys
import sqlite3
from flask import g

STATIC_URL = '/static/'
app = Flask(__name__, static_url_path='/static')
app.debug = True



DATABASE = 'database.db'


def connect_to_database():
    db = sqlite3.connect(DATABASE)

    c = db.cursor()
    
    try:
        c.execute('CREATE TABLE contacts (full_name text, email text, phone text)')
    except sqlite3.OperationalError:
        pass
    db.commit()

    return db


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/home/')
@app.route('/')
def index():
    return render_template('index.html', STATIC_URL=STATIC_URL)

@app.route('/aboutus/')
def about():
    return render_template('aboutus.html', STATIC_URL=STATIC_URL)

@app.route('/blackberry/')
def blackberry():
    return render_template('black.html', STATIC_URL=STATIC_URL)

@app.route('/grapes/')
def grapes():
    return render_template('grapes.html', STATIC_URL=STATIC_URL)

@app.route('/straw/')
def strawberry():
    return render_template('straw.html', STATIC_URL=STATIC_URL)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        

        full_name=request.form['full_name']
        email=request.form['email']
        phone=request.form['phone']

        # msg = render_template('email-template/email.html', name=full_name, email=email, phone=phone)
        #here you would actually send the email

        db = get_db()

        c = db.cursor()
        c.execute('INSERT INTO contacts (full_name, email, phone) VALUES (?,?,?)', (full_name, email, phone))
        db.commit()


        return 'OK'
    else:
        return render_template('contact.html', STATIC_URL=STATIC_URL)

if __name__ == '__main__':
    app.run()
