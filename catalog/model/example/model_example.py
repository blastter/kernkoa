#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This import import kernkoa so you can access the main scope
#   it's not necesary of you provide the database on the instantiation 
#   so you can port the model to other solutions that are not based on KernKoa
from kernkoa import *

class model_example:
    db = None
    def __init__(self, db = None):
        if db == None:
            self.db = dbs[config.defaultDatabase]
        else:
            self.db = db
    
    def checkTables(self):
        