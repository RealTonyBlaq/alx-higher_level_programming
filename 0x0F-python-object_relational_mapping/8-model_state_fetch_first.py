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
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    result = session.query(State).first()
    """
    session creates an instance of the class State with with results
    result in this case is an instance of State
    """
    if result is None:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))
