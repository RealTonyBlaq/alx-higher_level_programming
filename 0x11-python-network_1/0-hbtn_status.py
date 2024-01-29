#!/usr/bin/python3
""" Script that fetches a url """

from urllib.request import urlopen

url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print(f"\t- type: ")
