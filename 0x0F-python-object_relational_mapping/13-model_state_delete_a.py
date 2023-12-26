#!/usr/bin/python3
"""
Script deletes rows where the name column values have the letter 'a'
"""

from model_state import Base, State
from sqlalchemy import create_engine, delete
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    conn = engine.connect()
    statement = delete(State).where(State.name.like('%a%'))
    conn.execute(statement)
    conn.commit()
    conn.close()
