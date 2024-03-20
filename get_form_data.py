from flask import request

#signup form data
def signup_form_data():
    signup_data = {}
    
    signup_data['first_name'] = request.form['first_name'].strip().capitalize()
    signup_data['last_name'] = request.form['last_name'].strip().capitalize()
    signup_data['email_id'] = request.form['email_id'].strip().capitalize()
    signup_data['contact_number'] = request.form['contact_number'].strip().capitalize()
    
    return signup_data