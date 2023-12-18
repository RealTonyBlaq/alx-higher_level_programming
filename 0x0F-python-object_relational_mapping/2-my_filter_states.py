#!/usr/bin/python3
"""
Script queries a database using MySQLdb
retrieves data from a table states in a database
where name column has a string value passed as the
fourth argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               passwd=argv[1], db=argv[3])
    cur = database.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE name = '{}'\
                ORDER BY states.id ASC;".format(argv[4]))
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    database.close()
