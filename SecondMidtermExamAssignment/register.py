#!python.exe

import os, cgi
import base, authenticate

params = cgi.FieldStorage()

if os.environ['REQUEST_METHOD'].upper() == "POST":
    username = params.getvalue('username')
    password = params.getvalue('password')
    success = authenticate.register(username, password)
    if success:
        print('Location:login.py')


base.start_html()
print('''<form method="POST">
username <input type="text" name="username" />
password <input type="password" name="password"/>
<input type="submit" value="Register"/>
</form>''')
base.finish_html()