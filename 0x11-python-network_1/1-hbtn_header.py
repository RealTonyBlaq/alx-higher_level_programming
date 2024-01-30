#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""

import sys
from urllib.request import Request, urlopen

if __name__ == 
