#!/usr/bin/env python3
import os
import cgi

from secret import username, password

form = cgi.FieldStorage()

print("Content-Type: text/html")
if (username, password) == (form.getvalue("username"), form.getvalue("password")):
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()

print(form.getvalue("username"), form.getvalue("password"))
