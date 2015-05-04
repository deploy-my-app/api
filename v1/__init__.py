# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "tricci"
__date__ = "$30 avr. 2015 13:32:03$"

import os
import sys

def create_app():
	from flask import Flask, render_template
	from flask.ext.httpauth import HTTPBasicAuth
	from flask.ext.mongoengine import MongoEngine
	from flask_debugtoolbar import DebugToolbarExtension
	from v1.models import db
	#start the app
	app = Flask(__name__)
	#Load up the config
	#app.config.from_pyfile('config')
	app.config["MONGODB_SETTINGS"]={
		"db":"deploy"
	}
	app.config["SECRET_KEY"]="secretkey"
	app.config["DEBUG_TB_ENABLED"]=True
	#bootstrap the database
	db.init_app(app)
	#bootstrap everything else
	#auth = HTTPBasicAuth()
	toolbar=DebugToolbarExtension(app)

	from v1.routes import blueprint as DeployApi
	app.register_blueprint(DeployApi)
	
	print app.url_map
	return app
if __name__ == '__main__':
	create_app().run()