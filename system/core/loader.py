#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kernkoa import *
#MEJORA detectar / para sacar el directorio
class loader:
	def model(self, mod, folder = None):
		if folder != None:
			sys.path.insert(0,config.libs["model"] + "/" + folder)
		print(folder)
		#print repr(sys.path)
		mod_model = __import__(mod)
		modelo = getattr(mod_model, mod)
		inst_model = modelo()
		return inst_model
		
	def language(self, lang, folder = None):
		if folder != None:
			sys.path.insert(0, config.libs["language"] + "/" + folder)
		mod_lang = __import__(mod)
		language = getattr(mod_lang, 'es')
		return language
		
	def controller(self, mod, folder = None):
		if folder != None:
			sys.path.insert(0, config.libs["controller"] + "/" + folder)
		mod_module = __import__(mod)
		module = getattr(mod_module, mod)
		inst_module = module()
		return inst_module
	
	def printFormat(self, format, folder = None):
		print(config.libs["printFormat"] + "/" + folder)
		if folder != None:
			sys.path.insert(0, config.libs["printFormat"] + "/" + folder)
		mod_print = __import__(format)
		pFormat = getattr(mod_print, format)
		return pFormat
	
	def addon(self,module, component):
		mod = __import__(module)
		attrclass = getattr(mod, component)
		return attrclass
			
	

load = loader()
