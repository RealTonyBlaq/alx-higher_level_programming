#!/usr/bin/python3
"""
Script queries a database using MySQLdb
retrieves data from two tables 'states' and 'cities' in a database
by joining the two tables and accessing their keys
sorted by 'cities.id' value in ascending order

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               passwd=argv[1], db=argv[3])
    cur = database.cursor()
    arg = argv[4].split()
    cur.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = '{}'".format(arg[0])
                )
    data = cur.fetchall()
    for row in data:
        for col in row:
            print(col, end="")
            if col != data[-1][-1]:
                print(", ", end="")
    print()
    cur.close()
    database.close()
