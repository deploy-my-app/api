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
		

	app = Flask(__name__)
	from v1.routes import blueprint as DeployApi
	app.register_blueprint(DeployApi)
	auth = HTTPBasicAuth()
	print app.url_map
	return app