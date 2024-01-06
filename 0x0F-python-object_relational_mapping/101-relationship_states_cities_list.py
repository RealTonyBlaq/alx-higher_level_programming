#!/usr/bin/python3

"""
Script queries a database

This script will not be executed when imported
"""

from sqlalchemy import create_engine, select
from relationship_city import City
from relationship_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    with engine.connect() as connection:
        statement = select(State.id, State.name, City.id, City.name)\
            .join(State, State.id == City.state_id)\
            .order_by(State.id, City.id)
        result = connection.execute(statement)
        flag = 0
        for row in result:
            if flag == 0:
                print("{}: {}".format(row[0], row[1]))
                print("\t{}: {}".format(row[2], row[3]))
                copy = row[0]
                flag = 1
            elif flag == 1 and copy == row[0]:
                print("\t{}: {}".format())

