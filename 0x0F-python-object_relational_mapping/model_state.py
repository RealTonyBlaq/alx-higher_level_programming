#!/usr/bin/python3
""" Module """

from sqlalchemy import Table, String, MetaData, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost/hbtn_0e_6_usa', pool_pre_ping=True)
Base = declarative_base()
meta = MetaData()

class States(Base):
    """ Defining a class States which inherits from Base """
    id = Table("id", meta, Integer, unique=True, nullable=False,
               primary_key=True)
    