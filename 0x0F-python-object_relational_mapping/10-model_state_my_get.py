#!/usr/bin/python3
"""
Script queries a database using table objects to retrieve
all names with an 'a' in it
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    result = session.query(State).where(State.name == argv[4])
    if result is not None:
        print(result.id)
    else:
        print("Not found")
