#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#11.1
import zoo
zoo.hours()
Open 9-5 daily


# In[ ]:


#11.2
import zoo as menagerie
menagerie.hours()
Open 9-5 daily


# In[ ]:


#16.8
import sqlite3
conn = sqlite3.connect('books.db')
conn.execute('''CREATE TABLE books
             (title TEXT, author TEXT, year INTEGER)''')
conn.close()


from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
engine = create_engine('sqlite:///books.db')
metadata = MetaData()
books = Table('books', metadata,
              Column('title', String),
              Column('author', String),
              Column('year', Integer))
with engine.connect() as conn:
    metadata.create_all(engine)
    for row in conn.execute(books.select().order_by(books.c.title)):
        print(row.title)
        
engine.dispose()

