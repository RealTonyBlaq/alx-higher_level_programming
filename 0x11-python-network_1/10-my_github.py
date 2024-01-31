#!/usr/bin/python3
"""
Script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
argv[1] - Username
argv[2] - password (Personal Access Token)
"""
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://api.github.com/user"
    credentials = (argv[1], argv[2])
    r = requests.get(url=URL, auth=credentials)
    try:
        r.raise_for_status()

        data = r.json()
        userID = data.get("id")
        print(userID) if userID else print("None")
    except Exception:
        p
