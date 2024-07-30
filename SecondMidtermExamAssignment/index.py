#!python.exe

import os
from http import cookies
http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)


print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
</head>
<body>
<p>Hello''',get_all_cookies_object.get("email").value, '''</p>
    
</body>
</html>''')

index.py

