import atexit
import os
import sqlite3
import sys

from DAO import _Hats, _Suppliers, _Orders


class _Repository:
    def __init__(self):
     self._conn=sqlite3.connect(sys.argv[4])
     self.hat=_Hats(self._conn)
     self.supplier = _Suppliers(self._conn)
     self.order = _Orders(self._conn)

    def _close(self):
     self._conn.commit()
     self._conn.close()
     #os.remove(sys.argv[4]) #delete it!!!!!!!!!!

    def create_tables(self):
        cursor = self._conn.cursor()
        cursor.executescript("""
        CREATE TABLE hats ( 
           id       INTEGER  PRIMARY KEY,   
           topping  STRING   NOT NULL,
           supplier INTEGER  REFERENCES supplier(id),
           quantity INTEGER  NOT NULL
        );              
                      
        CREATE TABLE suppliers (
            id    INTEGER  PRIMARY KEY,   
            name  STRING   NOT NULL
        );
          
        CREATE TABLE orders (
            id       INTEGER  PRIMARY KEY,
            location STRING   NOT NULL,   
            hat      INTEGER  REFERENCES hat(id)
        );
        
     """)

    def deleteifExist(self):
        Data_Base_Exist = os.path.isfile('database.db')
        self.__init__()


repo = _Repository()
atexit.register(repo._close)


