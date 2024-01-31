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
    if len(argv) >= 2:
        letter = argv[1]
    else:
        letter = ""
    r = requests.post(url=url, data={"q": letter})
    try:
        js_object = r.json()
        id, name = js_object.get("id"), js_object.get("name")
        print("[{}] {}".format(id, name))
    except requests.exceptions.JSONDecodeError:
        if r.headers['content-type'] == "application/json":
            print("No result")
        else:
            print("Not a valid JSON")
