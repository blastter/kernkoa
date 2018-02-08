#!/usr/bin/env python
# -*- coding: utf-8 -*-

########
#
#	Created by Albin Trotter E.
#	Date: 05-09-2016
#	Last Modification: 06-02-2018
#
#	Why not to use it directly database libraries?
#	It's a way to standarize the different databases libraries, it's like an 
#	abstract, to make the methods common so you don't have to memorize al the
# 	different commands in each kind of database.
#
#######
import sqlite3
from array import * 
from collections import *

class sqlite:
	
	conn = None
	
	database = None
	
	autocommit = True
	
	def __init__(self, host, user, password, database):
		self.database = host
	
	def open(self):
		self.conn = sqlite3.connect(self.database)
	
	def close(self):
		self.conn.close();
	
	#	Function to execute any query to the database:
	#		- Select: it will return a table with the first row with the column names
	#		- Insert, Update and Delete: will return the number of affected rows.
	#		- Create: <----

	def query(self, query):
		query = query#.encode('utf-8')
		self.open()
		cur = self.conn.cursor()
		print(query)
		cur.execute(query)

		if "SELECT" in query.upper():
			data = []
			data = cur.fetchall()
			columndes = cur.description
			column = []
			for c in columndes:
				column.append(c[0])
			data.insert(0,column)
			self.close()
			return data
		elif "INSERT" in query.upper() or "UPDATE" in query.upper() or "DELETE" in query.upper():
			if self.autocommit:
				self.conn.commit()
			count = cur.rowcount
			self.close()
			return count
		return None
	
	# Get a dictionary with one column as key containing the row as dictionary.
	def nestedDictionary(self, query, column):
		data = self.query(query)
		cols = data[0]
		config = OrderedDict()
		for x in range(1, len(data)):
			field = None
			row = OrderedDict()
			for y in range(0,len(cols)):
				if cols[y] == column:
					field = data[x][y]
				try:
					row[cols[y]] = data[x][y]
				except:
					row[cols[y]] = ''
			config[field] = row
		return config

	# Starts a transaction to do multiples queries.
	def startTransaction(self):
		self.autocommit = False
	
	# Commit the queries waiting to be commited.
	def commitTransaction(self):
		self.con.commit()

	# Get a dictionary with the column as key and value of the column for one row
	#	If you use column as parameter it will return a nestedDictionary
	def getDictionary(self, query, **kwargs):
		if len(kwargs)>0:
			if "column" in kwargs:
				return self.nestedDictionary(query, kwargs["column"])
		data = self.query(query)
		info = OrderedDict()
		cols = data[0]
		if len(data) == 2:
			for x in range(0, len(cols)):
				info[cols[x]] = data[1][x]
		else:
			return False
		return info
	
	# Gets one value of one value query
	def getValue(self, query):
		data = self.query(query)
		print(repr(data))
		return data[1][0]

	# Checks if the table exists
	def checkTable(self, table):
		query = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='" + table + "'"
		data = self.getValue(query)
		if data > 0:
			return True
		return False