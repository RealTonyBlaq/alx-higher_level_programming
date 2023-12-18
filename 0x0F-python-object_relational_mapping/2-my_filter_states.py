#!/usr/bin/python3
""" Module """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               passwd=argv[1], )
