#!/usr/bin/python3

"""
Script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""

from urllib.request import Request, urlopen
import urllib.parse
from sys import argv


if __name__ == "__main__":
    value = {"email": argv[2]}
    value = urllib.parse.urlencode(value)
    value = value.encode('ascii')
    req = Request(url=argv[1], data=value)
    with urlopen(req) as response:
        header = response.headers
        print("Your email is: {}".format(header["email"]))
