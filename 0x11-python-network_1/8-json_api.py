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
    try:
        js = r.json()
        print("[{}] {}".format(js[0], js[1]))
    except requests.exceptions.JSONDecodeError:
        if r.status_code == 204:
            print("No result")
        else:
            print("Not a valid JSON")
