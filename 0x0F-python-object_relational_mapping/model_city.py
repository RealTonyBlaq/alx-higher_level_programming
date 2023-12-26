#!/usr/bin/python3

""" Module """

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    Defining the class City that links to the sql table 'cities'

    Class Attributes:
    -----------------

    __tablename__ (str): name of the table
    id (int): An auto-generated column with unique values, a primary key
            and non-null
    name (str): A string column of max 128 characters and cannot be null
    state_id (int): A column that cannot be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, nullable=False, primary_key=True, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'), nullable=False)
