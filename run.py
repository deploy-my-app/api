#!/usr/bin/python
from cherrypy import wsgiserver
from main import app

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 5000), d)

if __name__ == '__main__':
	try:
		print ("Starting server, please check logs for more information /var/log/the-deployer/deployer-deamon.log")
		server.start()
	except KeyboardInterrupt:
		print ("Stopping server")
		server.stop()