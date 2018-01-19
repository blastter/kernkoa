#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
	Configuration WebLine2
	Author:
			Albin Trotter E.
	Date:
			2016-08-29
	
	Configuration file.
'''

#session timeout in minutes
session_timeout = 60

#base
#Use in case of subfolder /kernkoa
base = ""

#path to KernKoa
path = "/usr/local/kernkoa"

#URL fo KernKoa in case of subfolder configuration on nginx add kernkoa/
url = "http://10.211.55.8/"

#Secret key for session id generation and other things
secretKey="development key"

#Data base configuration
#used on kernkoa.py
databases = {
#	SQLite configuration
#				"maindb":{
#							"driver": "sqlite", 
#							"host": "database.db", 
#							"user": "",
#							"password": "", 
#							"database": ""
#						},
#	MySQL Configuration
#				"<MySQLDBName>":{
#							"driver":"mysqldb",
#							"host": "<hostURL or IP>",
#							"user":"<DB Username>",
#							"password":"<DB Password>",
#							"database":"<Schema or Database>"
#						}
			}

#Paths to libraries.
#used on kerkoa.py and system/core/loader.py
libs = {
		"main": path,
		"catalog": path + "/catalog",
		"core": path + "/system/core",
		"controller": path + "/catalog/controller",
		"model": path + "/catalog/model",
		"language": path + "/catalog/language",
		"printFormat": path + "/catalog/print",
		"addon": path + "/system/addons"
		}


libsCelery = {
		"asynclibrary": path + "/catalog/controller/celeryexample"
}

#Default Module to load on index.
home = "./main/main"
				
#pdf path
pdfPath = path + "/pdfs"

#flask debug
flaskDebug = True