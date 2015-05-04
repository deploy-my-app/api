from flask import Flask
from flask import abort
from flask import jsonify
from flask import make_response
from flask import request
from flask import Blueprint
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api
from v1.controllers import *

blueprint = Blueprint('deployements_api',__name__,url_prefix='/api/v1.0')
api = Api()
api.init_app(blueprint)

#TODO implement controllers
api.add_resource(UserManager,'/users')
api.add_resource(UserListManager,'/users/<int:user_id>')

#this will only be used to update the status of a specific deployement on a specific server for a specific command
api.add_resource(CommandStatusManager,'/deploys/<int:deploy_id>/servers/<int_server_id>/commands/<int:command_id>/status')

#These routes are genral purpos routes for anybody external to manage their deploymenets ^^
api.add_resource(RoutineListManager,'/routines')
api.add_resource(RoutineManager,'/routines/<int:routine_id>/')

api.add_resource(DeployManager,'/deploys')
api.add_resource(DeployListManager,'/deploys/<int:deploy_id>')

api.add_resource(CommandManager,'/commands')
api.add_resource(CommandListManager,'/commands/<int:command_id>')

api.add_resource(ServerManager,'/servers')
api.add_resource(ServerListManager,'/server/<int:server_id>')

api.add_resource(StatusManager,'/status')
api.add_resource(StatusListManager,'/status/<int:status_id>')

#TODO implement specific authentification mecainismes
#these routes will only authorize post requests for now
api.add_resource(AuthBasicManager,'/auth/basic') #specific authentification manager
api.add_resource(AuthKeyManager,'/auth/key') #specific authentification manager
api.add_resource(AuthOauthManager,'/auth/oauth') #specific authentification manager
