#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from array import * 
from collections import *

class sqlite:
	
	conn = None
	
	database = None
	
	autocommit = True
	
	def __init__(self, host="database.db", user="", password="", database=""):
		self.database = host
	
	def open(self):
		self.conn = sqlite3.connect(self.database)
	
	def close(self):
		self.conn.close();
	
	def query(self, query):
		query = query.encode('utf-8')
		self.open()
		cur = self.conn.cursor()
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
				self.con.commit()
			count = cur.rowcount
			self.close()
			return count
		return None
	
	def config(self, query, column):
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