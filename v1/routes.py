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
api.catch_all_404s=True
api.init_app(blueprint)


api.add_resource(UserListManager,'/users')
api.add_resource(UserManager,'/users/<user_id>')

#this will only be used to update the status of a specific deployement on a specific server for a specific command
api.add_resource(JobManager,'/job/<job_id>')

#These routes are genral purpos routes for anybody
api.add_resource(RoutineListManager,'/routines')
api.add_resource(RoutineManager,'/routines/<routine_id>/')

api.add_resource(DeployListManager,'/deploys')
api.add_resource(DeployManager,'/deploys/<deploy_id>')

api.add_resource(CommandListManager,'/commands')
api.add_resource(CommandManager,'/commands/<command_id>')

api.add_resource(ServerListManager,'/servers')
api.add_resource(ServerManager,'/server/<server_id>')

api.add_resource(StatusListManager,'/status')
api.add_resource(StatusManager,'/status/<status_id>')

#TODO implement specific authentification mecainismes maybe better in laravel or what not
#these routes will only authorize post requests for now
api.add_resource(AuthBasicManager,'/auth/basic') #specific authentification manager
api.add_resource(AuthKeyManager,'/auth/key') #specific authentification manager
api.add_resource(AuthOauthManager,'/auth/oauth') #specific authentification manager


@app.route("/update/job/<job_id>")
def update_job(job_id):
  if JobManager.servers[server_id].jobs.current.id==job_id:
    JobManager.servers[server_id].jobs.done=job_id
    if JobManager.servers[server_id].jobs.queue:
      #TODO here we check if the job is finished on all other servers
      finished=False
      for srv in JobManager.servers:
        pass
      #now we pop the last job and put it as current job
      JobManager.servers[server_id].jobs.current=JobManager.servers[server_id].jobs.queue.pop()
      #TODO here we need to call the server