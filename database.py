#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('student.db')
print "Opened database successfully"

conn.execute('''CREATE TABLE STUDENTS
         (NAME          TEXT,
         ADDR           TEXT,
         CITY           TEXT,
         PIN            TEXT);''')
print "Table created successfully"

conn.close()