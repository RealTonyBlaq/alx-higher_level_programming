#!/usr/bin/python3
"""
Script queries a database using table objects to
retrieve the first row

"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    result = session.query(State).order_by(State.id).first()
    if result is None:
        print()
    else:
        print("{}: {}".format(result.id, result.name))
