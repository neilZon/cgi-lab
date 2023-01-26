#!/usr/bin/env python3
import os
import sys
import cgi

from templates import _wrapper, login_page, secret_page

print("Content-Type: text/html")
print()
print(login_page())

cookies = os.environ["HTTP_COOKIE"].split("; ")
cookie_dict = dict()
if len(cookies) > 1:
    for cookie_pair in cookies:
        c = cookie_pair.split("=")
        cookie_dict[c[0]] = c[1]

if "username" in cookie_dict and "password" in cookie_dict:
    print(secret_page(cookie_dict["username"], cookie_dict["password"]))
