#!/usr/bin/python3
""" Script that fetches a url """

if __name__ == "__main__":
    from urllib.request import urlopen

    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        c = response.read()
        print("Body response:")
        print(f'\t- type: {type(c)}\n\t\
            - content: {c}\n\t- utf8 content: {c.decode("ascii")}')
