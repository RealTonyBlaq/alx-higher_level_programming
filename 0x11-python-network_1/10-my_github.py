#!/usr/bin/python3
"""
Script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import requests
from sys import argv


if __name__ == "__main__":
     = {"email": argv[2]}
    r = requests.post(url=argv[1], data=data)
    print(r.text)
