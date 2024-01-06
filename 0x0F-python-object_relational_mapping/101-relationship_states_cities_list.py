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
        s_statement = select(State.id, State.name).order_by(State.id)
        c_statement = select(City.id, City.name).join(State, State.id == City.state_id).order_by(City.id)
        s_result = connection.execute(s_statement)
        c_result = connection.execute(c_statement)
        for row in s_result:
            print()
