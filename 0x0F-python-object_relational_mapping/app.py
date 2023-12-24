#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

engine = create_engine("mysql://root:root@localhost/database", pool_pre_ping=True)

metadata = MetaData()

table = Table("new", metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(50)),
              Column('email', String(70)))

metadata.create_all(bind=engine)

# Fetch table names
table_names = metadata.tables.keys()
for name in table_names:
    print(f'my table: {name}')
