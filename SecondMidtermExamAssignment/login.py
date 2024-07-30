#!python.exe

import mysql.connector # "C:\ProgramData\Anaconda3\python.exe" -m pip install mysql-connector 
import json
import os
from http import cookies
import cgi
import hashlib

db_conf = {
    "host":"localhost",
    "db_name": "obrana",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

params = cgi.FieldStorage()

def hash_password(password):
    password_bin = password.encode('utf-8')
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac(
        'sha256', password_bin, salt, 100000
    )
    return salt + hash

def create_user(email, password) :
    query = "INSERT INTO sessions (email, password) VALUES (%s, %s)"
    password1 = hash_password(password)
    values = (email, password1)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    
def get_user(email):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE email='" + str(email) + "'")
    myresult = cursor.fetchone()
    return myresult

def verify_password(password_plain_text, stored_password_hash):
    salt = stored_password_hash[:32]
    key = stored_password_hash[32:]
    new_hash = hashlib.pbkdf2_hmac('sha256', password_plain_text.encode('utf-8'), salt, 100000)
    return (key == new_hash)

if os.environ["REQUEST_METHOD"].upper() == "POST":
    user = get_user(params.getvalue("email"))
    if user is not None:
        if verify_password(params.getvalue('password'), user[2]):
            cookie = cookies.SimpleCookie()
            cookie['email'] = params.getvalue("email")
            print(cookie.output())

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<form action="" method="post">
  <label for="email">Email:</label>
  <input type="email" name="email" id="email"><br>

  <label for="password">Password:</label>
  <input type="password" name="password" id="password"><br>

  <input type="submit">
</form>''')
if user is None:
    print("User ne postoji")
if verify_password(params.getvalue('password'), user[2]) is False:
    print("Pogresna lozinka")

print('''</body>
</html>''')