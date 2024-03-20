from flask import Flask, render_template, redirect, url_for, request
import datetime

import get_form_data
import id_generator

app = Flask(__name__)
app.secret_key = 'jdjhd67d873hdihd38id38h'

@app.route('/')
def index():
    u_dt = datetime.datetime.utcnow()
    return render_template('index.html', utc_dt = u_dt )

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register_details():
    user_data = get_form_data.signup_form_data()
    print("form data = ", user_data)
    user_data['user_id'] = 
    user_data['regd_date'] = datetime.datetime.today()
    print("form data = ", user_data)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)