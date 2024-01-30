#!/usr/bin/python3
""" Script that fetches a url """

from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as response:
        c = response.read()
        print("Body response:")
        print('\t- type:', type(c))
        print('\t- content:', c)
        print('\t- utf8 content:', c.decode("utf-8"))
