"""
Entry point to our Api
"""
from flask import Flask, jsonify, abort, make_response, request
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api, Resource, reqparse

app = Flask(__name__)
auth = HTTPBasicAuth()

keys = [

	{
		"User_id":1,
		"public_key":"123456789", #is th epassword
		"private_key":"123456789" #is the hashing salt
	}

]
Servers=[

	{
		"id":1
		"hostname":"test.com",
		"ip":"192.168.33.10",
		"user_id":1
		"routines":[1]
	}

]
Command_Routines = [
	{
		"id":1,
		"commands":[
			"cd {{app}} ",
			"composer update"
		],
	},
	{
		"id":2,
		"commands":[
			"cd {{app}} ",
			"composer install"
		],
	}
]
Command_Routines_Status=[
	
	{
		"server_id":1, # key
		"routine_id":1, # key
		"commands":[
			{
				"command_id": 1,
				"status":"finished",
				"done":True,
				"output":"",
				"started_at":"28.04.2015 00.00.00",
				"finished_at":"28.04.2015 00.00.10",
				"tries":1
			},
			{
				"command_id": 2,
				"status":"processing",
				"done":False,
				"output":"",
				"started_at":"28.04.2015 00.00.00",
				"finished_at":"",
				"tries":1
			}
		],
		"status":"processing"
		
	},

]
class User:
	def __init__(self):
		self.id=1
		self.name="Thomas"
		self.password_hash="Hash this password later"
		self.private_key="123456789"
		self.public_key="987654321"

	def getPubKey(self):
		return self.public_key
	def getPrivateKey(self):
		return self.private_key
	def getRoutineStatus(self,id,server):
		return next((item for item in my_list if item['server_id'] == server_id and item["routine_id"]==routine_id), None)["status"]
@auth.verify_password
def verify_pw(username, password):
    return call_custom_verify_function(username, password)
@auth.get_password
def get_password(username):
    if username == 'thomas':
        return 'python'
    return None

@auth.error_handler(401)
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

class CommandListApi(Resource):
	def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('public_key', type = str, required = True, help = 'No task title provided', location = 'headers')
        self.reqparse.add_argument('commands', type = list, required=True, help="No commands provided to add to the deployement", location = 'json')
        super(CommandListApi, self).__init__()
    def get(self):
        

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

api.add_resource(TaskListAPI, '/api/v1.0/commands', endpoint = 'commands')
api.add_resource(TaskAPI, '/api/v1.0/commands/<int:id>', endpoint = 'command')

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