#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc
from array import * 
from collections import *

class mssql:
	con = None
	
	host = None
	user = None
	password = None
	database = None
	
	status = None
	
	constring = None
	
	autocommit = True
	
	def __init__(self, host="", user="", password="", database=""):
		try:
			self.con = pyodbc.connect("DSN=" + database + ";UID=" + user + ";PWD=" + password)
			cursor = self.con.cursor()
			cursor.execute("select 2+2 as [Result]")
			number  = cursor.fetchone()
			if number[0] == 4:
				self.status = "OK"
			else:
				self.status = "W"
		except pyodbc.Error, e:
			print "Error %d: %s" % (e.args[0],e.args(1))
			self.status = "Error"
			
		finally:
			if self.con:
				self.host = ""
				self.user = user
				self.password = password
				self.database = database
				self.constring = "DSN=" + database + ";UID=" + user + ";PWD=" + password
				self.con.close()
			#print self.status
	
	def open(self):
		try:
			self.con = pyodbc.connect(self.constring)
		except pyodbc.Error, e:
			print "Error %d: %s" % (e.args[0],e.args(1))
			self.status = "Error"
			
	def close(self):
		if self.con:
			self.con.close()
	
	def test(self):
		self.open()
		cur = self.con.cursor()
		cur.execute("select 1+1")
		data = cur.fetchone()
		self.close()
		if data[0] == 2:
			return True
		return  False

	def query(self, query):
		query = query.encode('utf8')
		#print query
		self.open()
		cur = self.con.cursor()
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
		
		

'''db = mssql()
if db.test():
	print "Conectado."
else:
	print "Error."
	
print db.query("select * from flexline.listaprecio where empresa = 'E10'")'''
