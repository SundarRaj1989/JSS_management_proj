from pymongo import MongoClient
from bson.objectid import ObjectId

def configure_db():
    global con
    global db_registration
    global col_user
    
    con = MongoClient("mongodb+srv://sraj81791sm:jss_2024@cluster0.9oizvew.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db_registration = con.jss_registration
    col_user = db_registration.users    
    col_emp = db_registration.employees
    return

def save_user_details(user_details):
    global col_user    
    configure_db()
        
    col_user.insert_one(user_details)
    return "User created Successfully"

def check_user_availability(email):
    global col_user
    configure_db()
    
    count_value = col_user.count_documents({'email_id': email })
    return count_value