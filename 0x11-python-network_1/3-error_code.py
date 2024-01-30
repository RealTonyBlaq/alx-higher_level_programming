#!/usr/bin/python3
"""
Script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

import urllib
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with 
