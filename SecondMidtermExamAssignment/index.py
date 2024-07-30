#!python.exe

import base
import cgi

params=cgi.FieldStorage()



base.start_html()
print('<form>')
print(params)
print('</form>')
base.finish_html()
