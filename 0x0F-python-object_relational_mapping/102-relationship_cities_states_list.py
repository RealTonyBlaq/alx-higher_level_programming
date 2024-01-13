#!/usr/bin/python3

"""
Script lists all City objects from the database using
the relationship between City and State
"""

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(argv[0], argv[1], argv))
