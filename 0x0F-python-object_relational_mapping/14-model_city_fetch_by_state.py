#!/usr/bin/python3

""" Module """

from model_city import Base, City
from sqlalchemy import create_engine
from sys import argv

engine = create_engine('mysql://{}:{}@localhost:3306/{}'.
                       format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
with engine.connect() as connection:
    
