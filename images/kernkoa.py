#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import of base libraries
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, send_file, Response, stream_with_context, current_app, has_request_context, make_response, jsonify
#from bson import json_util
from celery import Celery
#from flask_celeryext import RequestContextTask

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

#sys.path.insert(0, config.libs["controller"] + "/celeryexample")
#print(repr(sys.path[0]))



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
#configuring gevent for async tasks
app.config['BROKER_TRANSPORT'] = 'redis'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config["CELERY_TASK_SERIALIZER"] = "pickle"
app.config["CELERY_ACCEPT_CONTENT"] = ['pickle', 'json']
#creating instance for Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
from RequestContextTask import RequestContextTask
#---------


#execute async method giving instance
def exeTask(instance, method, params = None):
	print('exe')
	print(repr(params))
	if len(params) > 0:
		task = backgroundTask.delay(instance=instance, method=method, params=params)
	else:
		task = backgroundTask.delay(instance=instance, method=method)
	print('exe post')
	return {'type':'task', 'id': task.id}

#Background execution of task
@celery.task(base=RequestContextTask, bind=True)
def backgroundTask(self, *args, **kwargs):
	print(repr(args))
	print(repr(kwargs))
	moduleclass = ((str(type(kwargs["instance"])).replace("<class '", '')).replace("'>", '')).split(".")
	params = kwargs["params"]
	path = params["urlpath"].split("/")
	urlpath = ""
	for i in range(0,len(path)-3):
		urlpath += "/" + path[i]
	sys.path.insert(0,config.libs["controller"] + urlpath)
	globals()[moduleclass[0]] = __import__(moduleclass[0])
	if "dbs" in kwargs:
		dbs = kwargs["dbs"]
	self.update_state(state='inProgress', meta = {'method':kwargs["method"]})
	if "params" in kwargs:
		data = getattr(kwargs["instance"], kwargs["method"])(self, kwargs["params"])
	else:
		data = getattr(kwargs["instance"], kwargs["method"])(self)
	return {'status': 'COMPLETE', 'data': data}

#-------------

#Session section, configuration of time out.
@app.before_request
def permanent_session():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes = config.session_timeout)

#celery task status report and result path
@app.route('/status/<task_id>')
def taskstatus(task_id):
	print('status')
	task = backgroundTask.AsyncResult(task_id)
	if task.info:
		if 'data' in task.info.keys() and "status" in task.info.keys():
			#print "test"
			dataI = task.info["data"]
			#print repr(dataI)
			return json.dumps({ "status": task.status, "data": dataI })
		
		return json.dumps({"status":task.status, "state": task.info})
	return json.dumps({"status":'Running', "state": ''})

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

@app.route(config.base + "/", defaults={"path":""})
@app.route(config.base + "/<path:path>")
def allPath(path):
	print(path)
	urlPath = path.split("/")
	urllibrary = urlPath[len(urlPath)-3]
	urlclass = urlPath[len(urlPath)-2]
	urlmethod = urlPath[len(urlPath)-1]
	importPath = ""
	for i in range(0, len(urlPath)-3):
		importPath += "/" + urlPath[i]
	sys.path.insert(0, config.libs["controller"] + importPath)
	urlmodule = __import__(urllibrary)
	urlclasslib = getattr(urlmodule, urlclass)
	instance = urlclasslib()
	urlexecmethod = getattr(instance, urlmethod)
	if request.method == 'GET':
		params = request.args
	else:
		params = request.form
	paramsDict = {}
	for key, val in params.items():
		paramsDict[key] = val
	paramsDict["urlpath"] = path
	data = urlexecmethod(paramsDict)
	return data

for name,lib in config.libsCelery.items():
	print("loading " + name + "(" + lib + ")...")
	sys.path.insert(0,lib)
	globals()[name] = __import__(name)

#execute of the app when debuging.
#when you execute kernkoa.py directly form python it mounts an debug http server.

if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)
	

