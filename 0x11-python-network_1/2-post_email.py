#!/usr/bin/python3
"""
Script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""

from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    
