#!/usr/bin/python3

""" Module """

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    Defining the class City that links to the sql table 'cities'
    
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, nullable=False, primary_key=True, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'), nullable=False)
