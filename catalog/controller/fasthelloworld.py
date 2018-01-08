#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kernkoa import * #imports every varible from kernkoa (databases, loader, etc...).

class fastHelloClass: # the name of the class can be any name you want, except for the classes used un Flask, Werkzeug, KernKoa, Library you've imported, etc...
	def fastHelloWorld(self, params = None): #the function you want to execute
		return "hello world!!." #data to be displayed on the browser or to be send to de M2M solution (like IoT and other things).

	def fastHelloWorldWithParameters(self, params = None):
		if params == None:
			return "Hello World"
		returnData = ""
		for key, parameter in params.items():
			returnData = returnData + key + " = " + parameter + "<br>"
		return returnData