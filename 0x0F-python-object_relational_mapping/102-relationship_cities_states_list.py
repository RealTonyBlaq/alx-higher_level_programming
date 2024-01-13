#!/usr/bin/python3

"""
Script lists all City objects from the database using
the relationship between City and State
"""

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql://{}")
