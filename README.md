![alt text](https://raw.githubusercontent.com/blastter/kernkoa/master/images/kernkoachi.png)
# KernKoa

Kern = Kernel (German)

Koa = Kernel (Japanese)

## Contents
- [Definition](#definition)
- [DefautFolderStructure](#defaultfolderstructure)
- [Instalation](#instalation)
- [Configuration](#Configuration)
- [FastExample](#fastexample)
- [Debugging](#debugging)
- [Asynchronous](#asynchronous)

## Definition
KernKoa is an easy to use kernel (or BackBone if you prefer) for webservices, to develop fast webservices based applications (modules in KernKoa) in python, with dynamic routes calling libraries clases and methods using the URLs. The URL based calls make easy and to implement webpages or webservices in python so you don't have to configure complex route files and you can faste test you web applications.
KernKoa, now is implemented using Flask (microframework) as base to make the dynamic routing to generate instances of classes from a specific lybrary and the call methods with parameters. And it's runing on NGinX passing throw UWSGI.

Example (it doesn't work yet):

http://example.exmaple.com/folder/library/class/method?parameter1=value1&....&paramaterN=valueN

The KernKoa Project is designed to implement very modular solutions, and you can port from one kernkoa page or webservice to another easily if you have the standard configuration of databases and other things in the destination kernkoa server.
This backbone (or kerner if you prefer) is designed to use MVC to keep separate Models, Views (Templates using Werkzeug) and Controllers. In the configuration file (config.py) you can configure the paths to different folders to contain the different modules for controllers, models and templates.

## Defaut Folder Structure
Looking into the folder structure, you can define it as you want (in config.py) but the preconfigured is:

```
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
```


## Instalation:
1. Install of basics: python-virtualenv nginx g++ build-essential python3 python3-dev.

	```apt-get install python-virtualenv nginx g++ build-essential python3 python3-dev git```

2. Clone the project anywhere you want (/usr/local/ for less configuration)

	```git clone https://github.com/blastter/kernkoa.git```

3. Create the virtual environment with virtualenv inside the proyect.

	```virtualenv -p python3 venv3```

4. Activate the virtual environment.

	```. venv3/bin/activate```

	The console should look like:

	```(venv3) root@kernkoa:/usr/local/kernkoa#```

	The (venv3) before the loginpathroot what ever the name is, means that you are inside a virtual environment.

5. Install python libs:

	```pip install uwsgi flask```

	Te test it:
	```python kernkoa.py```
	Ther debug http server shoud be listening on port 5000.

6. Execute setup.sh. (if server already have nginx please don't execute this. Open de the script and omit the rm part for nginx).
	
	```sh setup.sh```

	It will install UWSGI service, create de configuration folders in etc, copy base configuration files, add kernkoa to UWSGI service and activate it. Also it will configure nginx to use root URL and restart it.
	
7. Test it.

	```http://<Server URL>/```

## Configuration:
There are two steps to configure KernKoa, the configuration of the project and the configuration of the server:
- Project configuration: is the configuration of each configuration files in the proyect. you can find 3 configuration files config.py, kernkoa_uwsgi.ini and kernkoa_nginx.conf.
	+ config.py: is the base configuration of KernKoa, here you can configure base path for the system, base URL, databases, folders names, name of the project (if you change it to other name), and so on. For more information read config.py file.
	+ kernkoa_uwsgi.ini: configuration of uwsgi fast cgi script, read it to change paramenters.
	+ kernkoa_nginx.conf: server and routing options for NGinX, read it to configure it.

## FastExample:
### Fast Hello World:
First you create a file (fasthelloworld.py) in the controller path that you've defined un de config.py file (default: "./catalog/controller/"), and then you use the information on the code below:

```python
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	from kernkoa import * #imports every varible from kernkoa (databases, loader, etc...).

	class fastHelloClass: # the name of the class can be any name you want, except for the classes used un Flask, Werkzeug, KernKoa, Library you've imported, etc...
		def fastHelloWorld(self, params = None): #the function you want to execute, self contained object to access object variables and functions, and params are the get (in url parameters after the ?) or post (form document sended by other mashine of from a web html form) parameters.
			return "hello world!!." #data to be displayed on the browser or to be send to de M2M solution (like IoT and other things).
```
The result of this function shuold for URL (http://<yourIPAddress:Port>/fasthelloworld/fastHelloClass/fastHelloWorld) be:

```
	hello world!!.
```

Then you enter to the url http://<yourIPAddress:Port>/fasthelloworld/fastHelloClass/fastHelloWorld
	You also can use parameters to print them or to check data, this is the example of a data function:

```python
	def fastHelloWorldWithParameters(self, params = None): #name of the function
		if params == None:#check of you have parameters, if you don't execute the next line, else continue the function
			return "Hello World" #return "hello world" to any system is calling the url if it doesn't has parameters
		returnData = "" #create a variable to return data
		for key, parameter in params.items(): #iterate each item un params and map them to key and parameter
			returnData = returnData + key + " = " + parameter + "<br>" #add text to returnData
		return returnData #return the content of returnData
```

The result of this function to url (http://<yourIPAddress:Port>/fasthelloworld/fastHelloClass/fastHelloWorldWithParameters?hello=world&with=parameters) should be:
```
		hello = world
		with = parameters
```
### Folder Example:
If you check the config.py file, you can read the folder path that has the controllers, kernkoa execute controllers and in the controller you can access the models and the templates if you wish to use MVC structure.
To create your own folder you just create the folder inside the controler folder and then you create a file with the same structure from the "FastHelloWorld" section.
I'll create the "examples" folder inside controller folder, then I'll create the "folderexmple.py" file inside and I'll put the same code of the "FastHelloWorld" section.

```python
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	from kernkoa import * #imports every varible from kernkoa (databases, loader, etc...).

	class fastHelloClass: # the name of the class can be any name you want, except for the classes used un Flask, Werkzeug, KernKoa, Library you've imported, etc...
		def fastHelloWorld(self, params = None): #the function you want to execute, self contained object to access object variables and functions, and params are the get (in url parameters after the ?) or post (form document sended by other mashine of from a web html form) parameters.
			return "hello world!!." #data to be displayed on the browser or to be send to de M2M solution (like IoT and other things).

	def fastHelloWorldWithParameters(self, params = None): #name of the function
		if params == None:#check of you have parameters, if you don't execute the next line, else continue the function
			return "Hello World" #return "hello world" to any system is calling the url if it doesn't has parameters
		returnData = "" #create a variable to return data
		for key, parameter in params.items(): #iterate each item un params and map them to key and parameter
			returnData = returnData + key + " = " + parameter + "<br>" #add text to returnData
		return returnData #return the content of returnData
```

And the result for the URL (http://<yourIPAddress:Port>/examples/folderexmple/fastHelloClass/fastHelloWorldWithParameters?hello=world&with=parameters) should be:

```
	hello = world
	with = parameters
```
For multiple folder please follow to folder1 to folder 7 in the controller folder.
example:

```http://<yourIPAddress:Port>/folder1/folder2/folder3/folder4/folder5/folder6/folder7/urllibrary/urlclass/urlmethod2?param1=1&param2=2&param3=3&param4=4```

Result:

```
param3 = 3
param1 = 1
param4 = 4
param2 = 2
```

## Debugging
As gods of programing probably don't need this, simple mortals like me need a lot of debugging, specilly when I forget to put the : after an if statement, a def or class definition.

### Development Environment
Just directly execute kernkoa in the virtual envioronment using:
```python kernkoa.py```
The debugging evioronment will start at port 5000. The changes will take efect everytime you modify a file, witch doesn't happens when you are in production envioronment where you have to restart the uwsgi service everytime you change a file in the project (systemctl restart emperor.uwsgi.service).

### Production environment

The log is configured in the kerkoa_wsgi.ini file, and the default path is "/var/log/uwsgi/kernkoa_uwsgi.log" normally I use ```less``` to read it, with shift + F to get the lastest errors. Also is recomended to use the print (some times with repr (get the array or dictionary content en raw format(Plain text))so you can see the information inside the variable) when something is failing.
The log path can be changed to any path you want, also if you don't have permisions to write to the log folder you can use the same path as kernkoa to write the log there.
Every time you modify any file you must execute the command ```systemctl restart emperor.uwsgi.service``` so uwsgi commit the changes on production environment(by restarting it).

## Asynchronous

Complex task are a great deal, when you are developing services. When a big complex task is executed, it takes over the main thread so the server won't responce new requests till the "big complex task" is finnished. Most of the problems happens when multiple clients, are calling request to you web page, they get stuck and get timeout error (when the task is to long to be executed on the main thread), till the server finnish the "big complex task" from the client that made the request and then listens again the other clients requests.
Because of "big complex tasks" (or just "complex task"), the comunity had created Celery wich is a asynchronous task manager wich executes the big complex tasks in other thread (process) or theads (processes) so the main thread (process) doesn't stop getting new requests from other clients while processing the complex task in other process.

KernKoa implements asynchronous task in a very simple way. You create two methods inside your module, one normal task to execute the asynchronous task and the asynchronous task that will be executed asynchronous. The normal task responce will be the asynchronous task id so the client ask for the state of the task, and with the same id when the task is ready the server will responce with the result of the big process.

The next example is of an asynchronous Task.
Creates in ./catalog/controller/celeryexample/asynclibrary/asyncclasstriggerfunction
URL to execute it is: ```http://<yourIPAddress:Port>/celeryexample/asynclibrary/asyncclass/triggerfunction```

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kernkoa import * #imports every varible from kernkoa (databases, loader, etc...).

# it's jus a normal class, wich has methods to be executed asynchronously
class asyncclass:
    
    # Trigger method to execute de big task.
    def triggerfunction(self, params = None):
        # exeTask is a method defined un KernKoa to execute async tasks
        #   It gets the name of the method to be executed un a string and the paramenters from
        #   the request (get or post).
        task = exeTask(self, "asyncfunction_celery", params)
        # The result of the method in this case is a URL to get the status of the Task.
        #   If the task has been succesfully procesed, the same link will give you the result
        return "<a href='" + config.url + "status/" + task["id"] + "'>Async Test"

    # Method to be executed asynchronously
    #   As you can see un the definition of the method you input celery_instance ans params
    #       - The params are the post parameters.
    #       - celery_instance is the connection to the task manager to update the status of the task.
    #           like when you change the done percentage of the task. 
    def asyncfunction_celery(self, celery_instance = None, params = None):
        #Counts to 10 with 2 seconds of delay so the task thread gets stuck, and the m
        for i in range(0,10):
            # if celery instance exists or if it's instansiated, it will update the result, if not, you are
            # runing on the main thread.
            if celery_instance:
                # Update of the status of the task.
                celery_instance.update_state(state="inProgress", meta={"number":i+1, "title": "Contando con 2 segundos de desfase hasta 10"})
            # Two second delay
            time.sleep(2)
            print(i)
        # The result of the async task.
        return i + 1
```


