#!/usr/bin/python3

"""
Script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""

from urllib.request import urlopen
import urllib.parse
from sys import argv


if __name__ == "__main__":
    value = {"email": argv[2]}
    value = urllib.parse.urlencode(value)
    value = value.encode('ascii')
    with urlopen(argv[1], value) as response:
        header = response.read()
        print("Your email is: {}".format(header.decode('utf-8')))
