#!/usr/bin/python3

""" Module """

from model_state import Base
from sqlalchemy import Table, Column, String, Integer


class City(Base):
    """ Defining the class City """
    __tablename__ = 'cities'
    id = Column('id', Integer, nullable=False, primary_key=True)
    
