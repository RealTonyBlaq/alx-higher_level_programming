#!/usr/bin/python3
"""
Script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    data = {"email": argv[2]}
    r = requests.post(url=argv[1], data=data)
    print("Your email is:", r.text)
