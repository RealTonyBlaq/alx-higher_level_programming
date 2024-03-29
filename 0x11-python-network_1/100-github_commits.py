#!/usr/bin/python3
"""
Script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
argv[1] - Repository name
argv[2] - owner name
"""
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://api.github.com/repos/{}/{}/commits"\
        .format(argv[2], argv[1])
    r = requests.get(URL)
    data = r.json()[:10]
    for key in data:
        print('{}: {}'.format(key['sha'], key['commit']['author']['name']))
