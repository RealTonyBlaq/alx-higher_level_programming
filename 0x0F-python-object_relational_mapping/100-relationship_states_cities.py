#!/usr/bin/python3

""" Module """

from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                       .format(argv[1], argv[2], argv[3]),
                       pool_pre_ping=True)

Session = sessionmaker(engine)
session = Session()
Base.metadata.create_all(engine)

new_state = State(name='California')
new_city = City(name='San Francisco')
new_state.cities.append(new_city)

session.add(new_state)
session.commit()
session.close()
