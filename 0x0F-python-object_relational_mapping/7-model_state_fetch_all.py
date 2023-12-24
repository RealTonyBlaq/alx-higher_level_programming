#!/usr/bin/python3
"""
Script queries a database using table objects to
retrieve the rows

"""

from model_state import Base, State
from sqlalchemy import create_engine, select
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    conn = engine.connect()
    statement = select(State)
    result = conn.execute(statement)
    for row in result:
        print("{}: {}".format(row[0], row[1]))
