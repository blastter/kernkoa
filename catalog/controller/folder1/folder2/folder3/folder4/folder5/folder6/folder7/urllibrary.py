#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kernkoa import * #imports every varible from kernkoa (databases, loader, etc...).

class urlclass: # the name of the class can be any name you want, except for the classes used un Flask, Werkzeug, KernKoa, Library you've imported, etc...
	def urlmethod(self, params = None): #the function you want to execute
		return "hello world!!." #data to be displayed on the browser or to be send to de M2M solution (like IoT and other things).

	def urlmethod2(self, params = None): #name of the function
		if params == None:#check of you have parameters, if you don't execute the next line, else continue the function
			return "Hello World" #return "hello world" to any system is calling the url if it doesn't has parameters
		returnData = "" #create a variable to return data
		for key, parameter in params.items(): #iterate each item un params and map them to key and parameter
			returnData = returnData + key + " = " + parameter + "<br>" #add text to returnData
		return returnData #return the content of returnData
