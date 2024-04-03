from flask import Flask, render_template, redirect, url_for, request
import datetime

import get_form_data
import id_generator

import authentication_db

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
    user_data['user_id'] = id_generator.random_alpha_numeric_id_with_currentYear(1, 5)
    user_data['regd_date'] = datetime.datetime.today()
    #check user availability
    user_email = user_data['email_id']
    user_id = user_data['user_id']
    check_user = authentication_db.check_user_availability(user_email, user_id)
    print('user availability = ', check_user)
    # status = authentication_db.save_user_details(user_data)
    return redirect(url_for('success', msg = check_user))

@app.route('/success/<msg>')
def success(msg):
    return render_template('success.html', msg = msg)


if __name__ == '__main__':
    app.run(debug=True)