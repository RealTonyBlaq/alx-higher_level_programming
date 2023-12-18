#!/usr/bin/python3
"""
Script queries a database using MySQLdb
retrieves data from the table 'states' in a database
where 'name' column has a string value passed as the
fourth argument, sorted by 'id' value in ascending order
and is also free from mySQL injections

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               passwd=argv[1], db=argv[3])
    cur = database.cursor()
    arg = argv[4].split()
    cur.execute("SELECT *\
                FROM states\
                WHERE BINARY name = '{}'\
                ORDER BY states.id ASC;".format(arg[0])
                )
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    database.close()
