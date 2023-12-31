#!/usr/bin/python3
""" Script uses sqlalchemy module to create a table in a database """

from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Defining a class State which inherits from Base

    class attributes:
    ------------------
    In addition to previous requirements:
    - cities have a relationship with the class cities
    - If a state object is deleted, all linked City objects
        will be deleted as well

    __tablename__ (str): name of the table
    id (int): An auto-generated column with unique values
    name (string): A column with string values which cannot be null
    """
    __tablename__ = "states"
    id = Column("id", Integer, unique=True, nullable=False,
                primary_key=True)
    name = Column("name", String(128), nullable=False)
