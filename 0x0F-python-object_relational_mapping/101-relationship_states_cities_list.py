#!/usr/bin/python3

"""
Script queries a database

This script will not be executed when imported
"""

from sqlalchemy import create_engine, select
from relationship_city import City
from relationship_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with engine.connect() as connection:
        statement = select(State.id, State.name, City.id, City.name)\
            .join(State, State.id == City.state_id)\
            .order_by(State.id, City.id)
        result = connection.execute(statement)
        flag = 0
        for row in result:
            if flag != 0:
                if copy != row[0]:
                    print("{}: {}".format(row[0], row[1]))
            else:
                print("{}: {}".format(row[0], row[1]))
                flag = 1
            if row[2] and row[3]:
                print("    {}: {}".format(row[2], row[3]))
            copy = row[0]
