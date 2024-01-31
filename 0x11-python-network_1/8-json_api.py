#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = ""
    r = requests.get()
    print(r.headers.get("X-Request-Id"))
