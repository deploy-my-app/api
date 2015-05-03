#!/usr/bin/env python
from flask import Flask, jsonify, abort, make_response, request
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api, Resource, reqparse

app = Flask(__name__)
auth = HTTPBasicAuth()
api = Api(app)
##Different examples of what will be stored in MongoDB, to be updated,m aybe with embeded documents
Users=[
  {
    "id":1,
    "name":"Thomas"
  }
]
keys = [

  {
    "user_id":1,
    "public_key":"123456789", #is the password
    "private_key":"123456789" #is the private password/unique data encryption key
  }

]
Servers=[

  {
    "id":1,
    "hostname":"test.com",
    "ip":"192.168.33.10",
    "user_id":1,
    "routines":[1]
  }

]
Routines = [
  {
    "id":1,
    "commands":[1,2],
    "status_id":1
  },
  {
    "id":2,
    "commands":[1,3],
    "status_id":2
  }
]
Commands=[
  {
    "id":1,
    "action":"cd {{app}}"
  },
  {
    "id":2,
    "action":"composer update"
  },
  {
    "id":3,
    "action":"composer install"
  },
  {
    "id":4,
    "action":"rm -rf {{app}}/storage"
  }
]
Statuses=[
  {
    "id":1,
    "name":"starting"
  },
  {
    "id":2,
    "name":"processing"
  },
  {
    "id":3,
    "name":"error"
  },
  {
    "id":4,
    "name":"finished without error"
  },
  {
    "id":5,
    "name":"finished with error"
  }
]
Command_Routines_Status=[

  {
    "server_id":1,
    "routine_id":1,
    "commands_id":1,
    "status":5,
    "done":True,
    "output":"",
    "started_at":"28.04.2015 00.00.00",
    "finished_at":"28.04.2015 00.00.10",
    "tries":1
  },
  {
    "server_id":1,
    "routine_id":1,
    "commands_id":2,
    "status":5,
    "done":True,
    "output":"",
    "started_at":"28.04.2015 00.00.00",
    "finished_at":"28.04.2015 00.00.10",
    "tries":1
  }

]

###############################################
# To be changed with the public key erification
"""
<<<<<<< HEAD
Entry point to our Api
"""
from flask import Flask
from flask.ext import restful

from v1 import deploy

app = Flask(__name__)
api = restful.Api(app)

api.add_resource()


if __name__ == '__main__':
    app.run(debug=True)

=======
@auth.verify_password
def verify_pw(username, password_hash):
  return call_custom_verify_function(username, password)
@auth.get_password
def get_password(username):
  if username == 'thomas':
    return 'python'
  return None
"""
"""
@auth.error_handler(401)
def unauthorized():
  return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler()
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)
"""
class CommandListApi(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('public_key', type = str, required = True, help = 'No task title provided', location = 'headers')
    self.reqparse.add_argument('commands', type = list, required=True, help="No commands provided to add to the deployement", location = 'json')
    super(CommandListApi, self).__init__()
  def get(self):
    pass

  def post(self):
    pass

class CommandApi(Resource):
  decorators=[auth.login_required]
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('public_key', type = str, required = True, help = 'No task title provided', location = 'json')
    self.reqparse.add_argument('commands', type = list, required=True, help="No commands provided to add to the deployement", location = 'json')
    self.reqparse.add_argument('done', type = bool, location = 'json')
    super(CommandApi, self).__init__()
  def get(self, id):
    pass

  def put(self, id):
    pass

  def delete(self, id):
    pass

#api.add_resource(TaskListAPI, '/api/v1.0/commands', endpoint = 'commands')
#api.add_resource(TaskAPI, '/api/v1.0/commands/<int:id>', endpoint = 'command')

"""
@app.route('/api/v1.0/commands',methods=["GET"])
@auth.login_required
def get_commands():
  return jsonify({"commands":Commands})
@app.route('/api/v1.0/commands',methods=["POST"])
def create_command():
  if not request.json and 'public_key' not in request.json and "commands" not in request.json:
    abort(400)
  command={
    "id":Commands[-1]["id"]+1,
    "public_key":request.json["public_key"],
    "commands":request.json["commands"],
    "done":False
  }
  Commands.append(command)
  return jsonify({"command":command}),201
@app.route('/api/v1.0/commands/<int:id>', methods=['GET'])
def get_command(id):
  command = [command for command in Commands if command["id"]==id]
  if len(command) == 0:
    abort(404)
  return jsonify({"command":command})
"""




if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 83e4221b5a3070bcf3d6795657c40c54b8f4ff90
