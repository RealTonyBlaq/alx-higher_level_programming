#!/usr/bin/python3
""" Module """

from sqlalchemy import Table, String, MetaData, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost:3306', pool_pre_ping=True)
Base = declarative_base()
meta = MetaData()

    """ Allows code to be imported before calling """


    class States(Base):
        """ Defining a class States which inherits from Base """
        __tablename__ = "states"
        id = Column("id", Integer, unique=True, nullable=False,
                primary_key=True)
        name = Column("name", String(128), nullable=False)

Base.metadata.create_all(engine)
