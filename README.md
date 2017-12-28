KernKoa

Kern = Kernel (German)
Koa = Kernel (Japanese)

Definition
KernKoa is an easy to use kernel (or BackBone if you prefer) for webservices to develop fast webservices based in python, with dinamic routes calling libraries clases and method using the URL. The URL based calls make easy and to implement webpages in python so you dont hav to configure complex route files and you can faste test you web application.
KernKoa, now is implemented using Flask (microframework) as base to make the dynamic routing to generate instances of classes from a specific lybrary and the call methos with parameters.
Exmample:
http://example.exmaple.com/folder/library/class/method?parameter1=value1&....&paramaterN=valueN

The KernKoa Proyect is designed to implement very modular solutions, and you can port from one kernkoa page or webservice to another easily if you have the correct configuration of databases and other things in the destination kernkoa server.
This backbone or kerner if you prefer is designed to use MVC to keep separate Models, Views (Templates using Werkzeug), Controllers. In the configuration file (config.py) you can configure the paths to different folder to contain the different modules for controllers, models and templates.

Looking into the folder structure, you can define it as you want (in config.py) but the preconfigured is:
|-KernKoaFolder
	|-catalog
	|	|-controller
	|	|-model
	|	|-print
	|-templates
	|-images
	|-pdfs
	|-system
	|	|-addons
	|	|-core

