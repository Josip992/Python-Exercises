import mysql.connector
import json
import password_pomoc

db_conf = {
    "host":"localhost",
    "db_name": "autentikacijaJosip",
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

def create_user(username, password):
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    hashed_password = password_pomoc.hash_password(password)
    values = (username, hashed_password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid 


def get_user(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE username='" + str(username) + "'")
    myresult = cursor.fetchone()
    return myresult