#!/usr/bin/env python3
import cgi
import cgitb
import json
import os
from templates import login_page, after_login_incorrect, secret_page
from secret import username, password
cgitb.enable(display=0, logdir="./logs")


#cgi.print_environ()



#print("Content-Type: application/json\n")
#print()
#print(json.dumps(dict(os.environ), indent=2))




form = cgi.FieldStorage()
username_log = form.getvalue("username")
password_log = form.getvalue("password")

if username_log == username and password_log == password:
    print("Set-Cookie:CorrectLogin = %s" % True)
    print('Content-Type: text/html')
    print()
else:
    print("Set-Cookie:CorrectLogin = %s" % False)
    print('Content-Type: text/html')
    print()
    print(after_login_incorrect())
   
   
## get cookie
cookie_string = os.environ.get('HTTP_COOKIE')

if cookie_string:
    cookie_pairs = cookie_string.split('; ')
    cookie = {}
    for pair in cookie_pairs:
        key, value = pair.split('=')
        cookie[key] = value
    if cookie.get('CorrectLogin') == 'True':
        print(secret_page(username, password))
    else:
        print(login_page())
else:
    print(login_page())

#if username_log is not None and password_log is not None:
#    print(f"<!doctype html><title>Login Form</title><h2>Hello {username}</h2>")
#    print(f"<p>Your password is {password}</p>")
