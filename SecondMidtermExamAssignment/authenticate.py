#!python.exe

import password_pomoc
import db

def register(username, password):
    user_id = db.create_user(username, password)
    if user_id:
        return True
    else:
        return False
