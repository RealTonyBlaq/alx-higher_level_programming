#!/usr/bin/python3
"""
Script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
and "q" as the key to the value of the argument passed.
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
    if r.headers['content-type'] == "application/json":
        js_object = r.json()
        id, name = js_object.get("id"), js_object.get("name")
        if name and id:
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
