#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, String, Integer

engine = create_engine("mysql://root:root@localhost/hbtn_0d_tvshows")

metadata = MetaData(engine)

table = Table("new", metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(50)),
              Column('email', String(70)))
metadata.create_all()
result = metadata.tables()
for row in result:
    print(f'my table: {row}')
