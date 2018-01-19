#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kernkoa import * 

class index:
	def index(self, params = None):
		return """<html>
					<head>
						<title>Hello World!</title>
						<style>
							body{
								background-color:black;
								color: red;
								text-align: center;
							}
						</style>
					</head>
					<body>
						<h1>KernKoa is working okay!.</h1>
					</body>
				  </html>"""