# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

#import mysql.connector
#import self as self
#from mysql.connector import cursor
#from mysqlx.protobuf.mysqlx_crud_pb2 import TABLE
#import sqlite3
#import os

from DTO import Hat, Supplier, Order
from Repository import repo

repo.deleteifExist()
repo.create_tables()

f = open(sys.argv[1], "r")
s = f.readline()
x = s.partition(",")
hat = (x[0])
for i in range(0, int(hat)):
    s = f.readline()
    y = s.split(",")
    repo.hat.insert(Hat(int(y[0]), y[1], int(y[2]), int(y[3])))

for i in range(0, int(x[2])):
    s = f.readline()
    y = s.split(",")
    suplierName=y[1]
    if (suplierName[len(suplierName) - 1] == '\n'):
        suplierName = suplierName[0:len(suplierName) - 1]
    repo.supplier.insert(Supplier(int(y[0]), suplierName))
f.close()
r = open(sys.argv[2], "r")
w = open(sys.argv[3], "w")

readText = r.read()
lines = readText.split("\n")
counter = 1
lines = readText.split("\n")
for line in lines:
    s = ""
    word = line.split(",")
    location = word[0]
    topping = word[1]
    list = repo.hat.findToppingSupplier(topping)
    hatId = repo.hat.findToppingId(topping)[0]
    currQuantity = repo.hat.findQuantity(hatId)[0]
    repo.hat.update(hatId, currQuantity - 1)
    if (currQuantity - 1 == 0):
        repo.hat.delete(hatId)

    repo.order.insert(Order(counter, location, hatId))
    counter += 1
    supplierId = list[0][0]
    suplierName = repo.supplier.find(supplierId)[0]
    if(suplierName[len(suplierName)-1]=='\n'):
        suplierName=suplierName[0:len(suplierName)-1]
   # print(suplierName[0:len(suplierName) - 2])
    if(counter>2):
        s ="\n"+ topping + "," + suplierName + "," + location
    else:
        s = topping + "," + suplierName+ "," + location
    w.write(s)
r.close()
w.close()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/