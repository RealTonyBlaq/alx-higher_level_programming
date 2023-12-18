#!/usr/bin/python3
""" Module """

import MySQLdb
import sys


db = MySQLdb.connect(host=locals, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute('SELECT * FROM tv_genres')
data = cur.fetchall()
for row in data:
    print(row)
