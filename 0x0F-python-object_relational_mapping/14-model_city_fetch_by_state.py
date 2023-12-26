#!/usr/bin/python3

""" Module """

from model_city import Base, City
from sqlalchemy import create_engine

engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format())
