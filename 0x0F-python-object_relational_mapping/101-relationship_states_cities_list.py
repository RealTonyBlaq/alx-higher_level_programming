#!/usr/bin/python3

"""
Script queries a database

This script will not be executed when imported
"""

from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    with engine.connect()
