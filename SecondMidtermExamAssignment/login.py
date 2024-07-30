#!python.exe

import os, cgi
import base, authenticate
import password_pomoc
from http import cookies
import db



params = cgi.FieldStorage()

if os.environ["REQUEST_METHOD"].upper() == "POST":
    user = db.get_user(params.getvalue('username'))
    if user is not None:
        if password_pomoc.verify_password(params.getvalue('password'), user[3]):
            cookie = cookies.SimpleCookie()
            cookie["username"] = params.getvalue("username")
            print(cookie.output())
            print('Location:index.py')

base.start_html()

print('''
<form action="" method="POST">
  <label for="username">Username:</label>
  <input type="username" name="username" id="username">
  <label for="password">Password:</label>
  <input type="password" name="password" id="password">
  <input type="submit" value="Login"/>
</form>
''')


if user is None:
    print("Korisnik sa unesenim usernameom ne postoji")
if password_pomoc.verify_password(params.getvalue('password'), user[3]) is False:
    print("Neispravna lozinka")
    print('Location:login.py')

base.finish_html()