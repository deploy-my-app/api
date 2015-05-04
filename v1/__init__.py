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
	app = Flask(__name__)

	#app.config.from_pyfile('config')
	app.config["MONGODB_SETTINGS"]={
		"db":"deploy"
	}
	app.config["SECRET_KEY"]="secretkey"
	db.init_app(app)
	auth = HTTPBasicAuth()
	toolbar=DebugToolbarExtension(app)

	from v1.routes import blueprint as DeployApi
	app.register_blueprint(DeployApi)
	
	print app.url_map
	return app