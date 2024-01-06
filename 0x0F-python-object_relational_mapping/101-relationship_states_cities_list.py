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
            .j
            .order_by(State.id, City.id)
        result = connection.execute(statement)
        for row in result:
            print("{}: {}".format(row[0], row[1]))
            c_statement = select(City.id, City.name)\
                .join(State, State.id == City.state_id)\
                .where(State.id == row[0]).order_by(City.id)
            c_result = connection.execute(c_statement)
            for _row in c_result:
                print("\t{}: {}".format(_row[0], _row[1]))
