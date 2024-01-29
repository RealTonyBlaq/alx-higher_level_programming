#!/usr/bin/python3
""" Script that fetches a url """
import urllib


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        c = response.read()
        print("Body response:")
        print('    - type: {}\n    - content: {}\n    - utf8 content: {}'
              .format(type(c), c, c.decode("utf-8")))
