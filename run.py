#!/usr/bin/python
from cherrypy import wsgiserver
from v1 import create_app


app = create_app()
app.run(debug=True,port=8080,host="0.0.0.0")
"""
d = wsgiserver.WSGIPathInfoDispatcher({'/': create_app()})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 5000), d)

if __name__ == '__main__':
	try:
		print ("Starting server, please check logs for more information /var/log/the-deployer/deployer-deamon.log")
		server.start()
	except KeyboardInterrupt:
		print ("Stopping server")
		server.stop()
"""