#!/usr/bin/python3
"""
Script uses MySQLdb module to query a database
It selects all values from a table called 'states'
where values in the 'name' column starts with a
capital 'N' and sorts it by their 'id' value in
ascending order.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3])
    cur = database.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE name LIKE BINARY 'N%'\
                ORDER BY states.id ASC;"
                )
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    database.close()
