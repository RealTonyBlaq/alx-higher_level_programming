#!/usr/bin/python3
""" Script that fetches a url """

if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        c = response.read()
        print("Body response:")
        print('    - type: {}\n    - content: {}\n    - utf8 content: {}'
              .format(type(c), c, c.decode("utf-8")))
