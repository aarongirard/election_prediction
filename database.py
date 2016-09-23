import sqlite3 as sql
import os, sys

"""
hacking way to access db because need abs ref to
this file, but when called from another file in different folder
there are issues

so to call, if not in root program dir, need to add ../ for
each sub directory
"""

#create database
def _create_StateElectoralCollege_table(db_path): 
  DBNAME = 'prediction.db'
  DBNAME = db_path + DBNAME
  DBNAME = os.path.realpath(DBNAME)
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
def add_record_StateElectoralCollege_table(values,db_path):
  DBNAME = 'prediction.db'
  DBNAME = db_path + DBNAME
  DBNAME = os.path.realpath(DBNAME)
  with sql.connect(DBNAME, timeout=30.0) as connection:
    c = connection.cursor()
    values = (values['time'],values['state'],
      values['name'],values['lastcloseprice'])
    
    c.execute('INSERT INTO StateElectoralCollege'
      '(time,state,name,lastcloseprice)' 
      'VALUES (?,?,?,?)', values)
    connection.commit()

def get_most_recent_record_foreach_state(db_path):
  DBNAME = 'prediction.db'
  DBNAME = db_path + DBNAME
  DBNAME = os.path.realpath(DBNAME)
  print DBNAME
  with sql.connect(DBNAME) as connection:
    c = connection.cursor()
    c.execute('select name, state,' 
      'max(time),lastcloseprice '
      'from StateElectoralCollege ' 
      'group by state, name')
    results = c.fetchall()
    return results


    
