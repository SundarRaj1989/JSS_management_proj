from flask import Flask, render_template, redirect
import datetime

app = Flask(__name__)
app.secret_key = 'jdjhd67d873hdihd38id38h'

@app.route('/')
def index():
    u_dt = datetime.datetime.utcnow()
    return render_template('index.html', utc_dt = u_dt )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)