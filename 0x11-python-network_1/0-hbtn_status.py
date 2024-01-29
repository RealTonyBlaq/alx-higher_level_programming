#!/usr/bin/python3
""" Script that fetches a url """
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as response:
        c = response.read()
        print("Body response:")
        print('    - type: {}\n    - content: {}\n    - utf8 content: {}'
              .format(type(c), c, c.decode("utf-8")))
