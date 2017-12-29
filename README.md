![alt text](https://raw.githubusercontent.com/blastter/kernkoa/master/images/kernkoachi.png)
# KernKoa

Kern = Kernel (German)

Koa = Kernel (Japanese)

## Contents
- [Definition](#definition)
- [DefautFolderStructure](#defaultfolderstructure)
- [Instalation](#instalation)
- [Configuration](#Configuration)

## Definition
KernKoa is an easy to use kernel (or BackBone if you prefer) for webservices to develop fast webservices based in python, with dinamic routes calling libraries clases and method using the URL. The URL based calls make easy and to implement webpages in python so you dont hav to configure complex route files and you can faste test you web application.
KernKoa, now is implemented using Flask (microframework) as base to make the dynamic routing to generate instances of classes from a specific lybrary and the call methods with parameters. And it's runing on NGinX passing throw UWSGI.

Example:

http://example.exmaple.com/folder/library/class/method?parameter1=value1&....&paramaterN=valueN

The KernKoa Proyect is designed to implement very modular solutions, and you can port from one kernkoa page or webservice to another easily if you have the correct configuration of databases and other things in the destination kernkoa server.
This backbone or kerner if you prefer is designed to use MVC to keep separate Models, Views (Templates using Werkzeug), Controllers. In the configuration file (config.py) you can configure the paths to different folder to contain the different modules for controllers, models and templates.

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

3. Create the virtual envioroment with virtualenv inside the proyect.

	```virtualenv -p python3 venv3```

4. Activate the virtual envioroment.

	```. venv3/bin/activate```

	The console should look like:

	```(venv3) root@kernkoa:/usr/local/kernkoa#```

	The (venv3) before the loginpathroot what ever the name is, means that you are inside a virtual envioronment.

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
