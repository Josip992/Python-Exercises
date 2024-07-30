#!python
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


if os.environ["REQUEST_METHOD"].upper() == "POST":
    user = get_user(params.getvalue("email"))
    if user is None:
        create_user(params.getvalue("email"), params.getvalue("password"))
        cookie = cookies.SimpleCookie()
        cookie['email'] = params.getvalue("email")
        print(cookie.output())
        print("location: index5.py")

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
    table, th, tr, td {
        border: 1px solid
        }
    </style>
</head>
<body>
    <form action ="" method="post">
    <table>
        <tr>
            <th>email:</th>
            <td><input type="email" name="email" value=""> </td>
        </tr>
        <tr>
            <th>password:</th>
            <td><input type="password" name="password" value=""> </td>
        </tr>
        <tr>
            <th><input type="submit"></th>
            <td></td>
        </tr>
    </table>
</form>''')
if user is not None:
    print("User postoji")

print('''</body>
</html>''')