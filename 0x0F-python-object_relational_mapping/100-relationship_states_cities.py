#!/usr/bin/python3

""" Module """

from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sys import argv
from sy

engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                       .format(argv[1], argv[2], argv[3]),
                       pool_pre_ping=True)

with engine.connect() as connection:
    Base.metadata.create_all(bind=engine)
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    connection.execute(new_state)
