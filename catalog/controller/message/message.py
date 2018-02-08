#!/usr/bin/env python
# -*- coding: utf-8 -*-

########
#            Code Written by: Albin Trotter E.
#            Date: 07-02-2018
#            Las Modification: 07-02-2018
#            URL: https://github.com/blastter/kernkoa
#            File: message/message.py
#            Part of: message module
#            Goal: It's a form for an example for the KernKoa Project.
########

from kernkoa import * #imports every varible from kernkoa (databases, loader, etc...).

class message:
    def index(self, params = None):
        mmessage = load.model("model_message", "message")
        messages = mmessage.get(limit = 50, order = 'desc')
        return render_template("message/index.html", messages = messages, formurl = config.url + "message/message/message/insert")
    
    def insert(self, params = None):
        print(repr(params))
        mmessage = load.model("model_message", "message")
        result = mmessage.insert(params)
        error = {}
        if len(params["message"]) > 1000:
            error["message"] = "You've passed maximum text length."
        if len(params["user"]) > 100:
            error["user"] = "Your nickname is too long."
        if len(error) > 0:
            return jsonify({"status": "error", "errors": error})
        if result:
            return jsonify({"status": "OK", "inserted": result})
        return jsonify({"status": "Error"})
    