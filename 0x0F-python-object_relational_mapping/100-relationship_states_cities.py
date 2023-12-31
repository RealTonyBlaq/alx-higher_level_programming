#!/usr/bin/python3

""" Module """

from sqlalchemy import create_engine, select
from relationship_city import Base, City
from relationship_state import Base, State
from sys import argv

engine = create_engine("mysql://{}:{}")
