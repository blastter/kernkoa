#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mysql
from array import * 
from collections import *

class mysqldb:
	con = None
	
	host = None
	user = None
	password = None
	database = None
	
	status = None
	autocommit = True
	
	def __init__(self, host = "", user = "", password = "", database = ""):
		
		try:
			self.con = mysql.connect(user = user, password = password, host = host, database = database)
		except mysql.Error as err:
			print(err)
		finally:
			if self.con:
				self.host = host
				self.user = user
				self.password = password
				self.database = database
				self.close()
	
	def open(self):
		if not self.con:
			try:
				self.con = mysql.connect(user = self.user, password = self.password, host = self.host, database = self.database)
			except mysql.connector.Error as err:
				print(err)
	
	def close(self):
		if self.con:
			self.con.close()
			self.con = None
	
	def query(self, query):
		query = query.encode('utf8')
		
		self.open()
		
		cur = self.con.cursor()
		cur.execute(query)
		
		if b"SELECT" in query[:10].upper():
			data = []
			data = list(cur.fetchall())
			columnes = cur.description
			#print(repr(columnes))
			column = []
			for c in columnes:
				column.append(c[0])
			data.insert(0, column)
			self.close()
			return data
		elif b"INSERT" in query.upper() or b"UPDATE" in query.upper() or b"DELETE" in query.upper():
			if self.autocommit:
				self.con.commit()
			count = cur.rowcount
			self.close()
			return count
		return None
	
	def config(self, query, column):
		data = self.query(query)
		if not data:
			return False
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
		
	def getDictionary(self, query):
		data = self.query(query)
		info = OrderedDict()
		cols = data[0]
		if len(data) == 2:
			for x in range(0, len(cols)):
				info[cols[x]] = data[1][x]
		else:
			return False
		return info
	
	def checkTable(self, tableName, database = None):
		query = """SELECT count(*)
					FROM information_schema.tables
					WHERE table_schema = '""" + database + """'
					AND table_name = '""" + tableName + """'"""
		if self.query(query)[1][0]>0:
			return True
		return False
		

"""db = mysqldb("localhost", "fono", "96omy7bc", "fono")
print repr(db.config("show tables like 'webpay'", "uid"))"""
