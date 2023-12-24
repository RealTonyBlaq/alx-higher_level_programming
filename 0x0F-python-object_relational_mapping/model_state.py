#!/usr/bin/python3
""" Module """

from sqlalchemy import Table, String, MetaData, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost/hbtn_0e_6_usa', pool_pre_ping=True, port=3306)
Base = declarative_base()
meta = MetaData()

class States(Base):
    """ Defining a class States which inherits from Base """
    id = Column("id", Integer, unique=True, nullable=False,
               primary_key=True)
    name = Column("name", String(128), nullable=False)

Base.metadata.create_all(engine)
