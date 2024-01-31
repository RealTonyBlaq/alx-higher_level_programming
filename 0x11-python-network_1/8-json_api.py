#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if argv[1]:
        q = argv[1]
    else:
        q = ""
    r = requests.post(url=url, data=q)
    if 
