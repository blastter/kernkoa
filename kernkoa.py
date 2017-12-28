#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import of base libraries
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, send_file, Response, stream_with_context, current_app, has_request_context, make_response, jsonify
#from bson import json_util
from datetime import timedelta
import datetime
import json
import config
import sys
import os
import os.path
import time
from importlib import reload

reload(sys)
#sys.setdefaultencoding("utf-8")
#set of path to templates
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

#configuration of secret key for encrytion of session data
SECRET_KEY = config.secretKey

#Load basic paths for KernKoa folders libs from config.py
for name,lib in config.libs.items():
	print("loading " + name + "(" + lib + ")...")
	sys.path.insert(0,lib)

#import library to load models, controlles, formats, etc..
#this library is in th system/core folder
from loader import *

#load of databases from config.py file
dbs = {}
for name, val in config.databases.items():
	print("loading database " + name + "...")
	mod = __import__(val["driver"])
	cl = getattr(mod, val["driver"])
	dbs[name] = cl(val["host"], val["user"], val["password"], val["database"])

#creating instance of flask app
app = Flask(__name__)
app.debug = config.flaskDebug
app.config.from_object(__name__)

#Session section, configuration of time out.
@app.before_request
def permanent_session():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes = config.session_timeout)

#default url when no folder specified in this case is in the controller class
#index.py
@app.route('/')
def index():
	print("/")
	module = __import__("index")
	clase = getattr(module, "index")
	instance = clase()
	params = None
	if request.method == 'GET':
		params = request.args
	else:
		params = request.form
	return instance.index(params);

#image folder
@app.route(config.base + "/images")
def image():
	if (request.args.get('image')[-3:]).upper() == 'GIF':
		return send_file("./images/" + request.args.get('image'), mimetype='image/gif')
	if (request.args.get('image')[-3:]).upper() == 'PNG':
		return send_file("./images/" + request.args.get('image'), mimetype='image/png')
	if (request.args.get('image')[-3:]).upper() == 'JPG':
		return send_file("./images/" + request.args.get('image'), mimetype='image/jpg')

#PDF Folder
@app.route(config.base + "/pdf")
def pdf(pdf = None):
	if pdf != None:
		return send_file(config.path + "/pdfs/" + pdf, mimetype="application/pdf")
	return send_file("./pdfs/" + request.args.get('pdf'), mimetype="application/pdf")

#two subfolder parameters
@app.route(config.base + '/<library>/<classes>', methods=['GET', 'POST'])
def methods(library, classes):
	lasturl = library + "/" + classes
	
	if library == "status":
		return taskstatus(classes)
	
	if library == "pdfs":
		return pdf(classes)
	
	module = __import__(library)
	clase = getattr(module, classes)
	instance = clase()
	params = None
	
	if request.method == 'GET':
		params = request.args
	else:
		params = request.form
		
	data = instance.index(params)
	return data

#three subfolder parameters
@app.route(config.base + '/<library>/<classes>/<method>', methods=['GET', 'POST'])
def classes(library, classes, method):
	lasturl = library + "/" + classes + "/" + method
	print(lasturl)
	module = __import__(library)
	clase = getattr(module, classes)
	instance = clase()
	meth = getattr(instance, method)
	params = None
	if request.method == 'GET':
		params = request.args
	else:
		params = request.form
	#print params
	
	data = meth(params)
	return data

#four subfolder parameters
@app.route(config.base + '/<folder>/<library>/<classes>/<method>', methods=['GET','POST'])
def folder(folder, library, classes, method):
	lasturl = folder + "/" + library + "/" + classes + "/" + method
	print(lasturl)
	sys.path.insert(0,config.libs["controller"] + "/" + folder)
	module = __import__(library)
	clase = getattr(module, classes)
	instance = clase()
	meth = getattr(instance, method)
	#print repr(request.form)
	if request.method == 'GET':
		params = request.args
	else:
		params = request.form
	
	data = meth(params)
	return data

#execute of the app when debuging.
#when you execute kernkoa.py directly form python it mounts an debug http server.
if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)
	

