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
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC;"
                )
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    database.close()
