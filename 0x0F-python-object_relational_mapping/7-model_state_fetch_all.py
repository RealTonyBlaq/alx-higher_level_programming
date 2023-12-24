#!/usr/bin/python3
""" Script queries a database """

from model_state import Base, State
from sqlalchemy import create_engine, MetaData, select
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    conn = engine.connect()
    statement = select((State.__tablename__)
    result = conn.execute(statement)
    for row in result:
        print(row)
