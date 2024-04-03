from flask import Flask, render_template, redirect, url_for, request, flash
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
    email = user_data['email_id']
    account_existance_check = authentication_db.check_user_availability(email)
    if account_existance_check:
        print('User already exists')
        flash("User already exists!! You need to Login")
        return redirect(url_for('login'))
    else:
        print('New user')
        cy = datetime.datetime.today()
        current_year = cy.strftime("%y") 
        user_data['regd_date'] = cy
        user_data['user_id'] = id_generator.random_alpha_numeric_id_with_currentYear(1, 5, current_year)
        msg = authentication_db.save_user_details(user_data)
        flash(msg)
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)