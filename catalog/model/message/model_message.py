#!/usr/bin/env python
# -*- coding: utf-8 -*-

########
#            Code Written by: Albin Trotter E.
#            Date: 07-02-2018
#            Las Modification: 07-02-2018
#            URL: https://github.com/blastter/kernkoa
#            File: message/model_message.py
#            Part of: message module
#            Goal: It's a form for an example for the KernKoa Project.
########

# This import import kernkoa so you can access the main scope
#   it's not necesary of you provide the database on the instantiation 
#   so you can port the model to other solutions that are not based on KernKoa
from kernkoa import *

class model_message:
    db = None
    def __init__(self, db = None):
        if db == None:
            self.db = dbs[config.defaultDatabase]
        else:
            self.db = db
        self.checkTables()
    
    def checkTables(self):
        if not self.db.checkTable("messages"):
            create = """CREATE TABLE messages(
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            user VARCHAR(100) NOT NULL,
                            message VARCHAR(1000) NOT NULL,
                            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )"""
            self.db.query(create)
    
    def insert(self, data):
        insert = """INSERT INTO messages (user, message) VALUES ('""" + data["user"] + """','""" + data["message"] + """')"""
        result = self.db.query(insert)
        if result > 0:
            return result
        return False
    
    def get(self, **kwargs):
        select = """select * from messages"""
        if "user" in kwargs:
            if "where" in select:
                select += " and"
            select += " user like '%" + kwargs["user"] + "%'"
        if "message" in kwargs:
            if "where" in select:
                select += " and"
            select += " message like '%" + kwargs["user"] + "%'"
        if "order" in kwargs:
            select += " order by id " + kwargs["order"]
        if "limit" in kwargs:
            select += " limit " + str(kwargs["limit"])

        print(select)
        
        data = self.db.getDictionary(select, column = "id")
        return data