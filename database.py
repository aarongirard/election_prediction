import sqlite3 as sql
import os

DBNAME = os.path.realpath('prediction.db')

#create database
def _create_StateElectoralCollege_table(): 
    #TIME_UTC,STATE,NAME, LASTCLOSEPRICE
    with sql.connect(DBNAME) as connection:
      c = connection.cursor()
      c.execute('CREATE TABLE StateElectoralCollege'
        '(time INTEGER NOT NULL, ' 
        'state TEXT NOT NULL,'
        'name TEXT NOT NULL,'
        'lastcloseprice REAL NOT NULL)')
      connection.commit() #commit insertion to DB

#values = {time,state,name,lastcloseprice}
#          int | txt | txt| float
def add_record_StateElectoralCollege_table(values):
  with sql.connect(DBNAME) as connection:
    c = connection.cursor()
    values = (values['time'],values['state'],
      values['name'],values['lastcloseprice'])
    
    c.execute('INSERT INTO StateElectoralCollege'
      '(time,state,name,lastcloseprice)' 
      'VALUES (?,?,?,?)', values)
    connection.commit()

def get_most_recent_record_foreach_state():
  with sql.connect(DBNAME) as connection:
    c = connection.cursor()
    c.execute('INSERT INTO StateElectoralCollege'
      '(time,state,name,lastcloseprice)' 
      'VALUES (?,?,?,?)', values)
    results = c.fetchall()
    return results