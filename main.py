from flask import Flask
from flask import render_template, render_template_string
from flask import request
import sys

STATIC_URL = '/static/'
app = Flask(__name__, static_url_path='/static')
app.debug = True



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

        msg = render_template('email-template/email.html', name=full_name, email=email, phone=phone)


        #here you would actually send the email
        pass

        return 'OK'
    else:
        return render_template('contact.html', STATIC_URL=STATIC_URL)

if __name__ == '__main__':
    app.run()
