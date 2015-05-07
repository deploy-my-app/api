from flask import abort
from flask import jsonify
from flask import make_response
from flask import request

from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from v1.models import *
from v1.decorators import *




#Manage all users
class UserListManager(Resource):
  def __init__(self):
    parser=reqparse.RequestParser()
    parser.add_argument("username",type=str,required=True)
    parser.add_argument("password",type=str,required=True)
    self.parser=parser
    self.users=User
  def get(self):
    
    d=[]
    for user in User.objects:
      d.append( {"id":str(user["id"]),"username":user["username"]} )
    return d
  def post(self):
    args=self.parser.parse_args()
    user,created=User(username=args["username"],password=args["password"]).save()
    if created:
      return {"id":str(user["id"])},200
    return {"error":"Error creating user"}
#Manage a specific User
class UserManager(Resource):
  """docstring for UserListManager"""
  def __init__(self):
    self.user=User
  def get(self,user_id):
    user = User.objects.get_or_404(id=user_id)
    try:
      if request.args.get('field'):
        
        field=request.args.get('field')
        if field in User._fields:
          return {field:str(user[field])}
        else:
          raise Exception("The field wasn't found in the user model")
      
      return {"id":str(user["id"]),"username":user["username"]}
    except Exception as e:
      return {"error":e.message},400
    
    
    


#The holy grail class that will run the core of this huge mess
class JobManager(Resource):
  """docstring for CommandStatusManager"""
  def __init__(self):
    self.servers=Server.objects
  #retrieves all the details for a command status
  def get(self,job_id):
    pass
  #creates a new command status
  def post(self,job_id):
    pass
  #updates a command status
  def put(self,job_id):
    parser=reqparse.RequestParser()
    parser.add_argument("key",type=str,required=True)
    parser.add_argument("value",type=str,required=True)
    args=parser.parse_args()

    key=args['key']
    value=args['value']
    job=Job.objects(id=job_id).first_or_404()
    if key == "status":
      value=Status.objects(id=value).first_or_404()
    elif key == "server":
      value = Server.objects(id=value).first_or_404()
    elif key == "deployement":
      value = Deploy.objects(id=value).first_or_404()
    job[key]=value







class RoutineListManager(Resource):
  """docstring for RoutineManager"""
  def __init__(self):
    pass
  def get(self):
    return Routine.objects.all().to_json()
  def post(self):
    parser=reqparse.RequestParser()
    parser.add_argument("name",type=str,required=True)
    parser.add_argument("user_id",type=str,required=True)
    args=parser.parse_args()
    user=User.objects(id=args["user_id"]).get_or_404()
    routeine=Routine(name=args["name"],user=user)
class RoutineManager(Resource):
  """docstring for RoutineListManager"""
  def __init__(self):
    pass
  def get(self,routine_id):
    pass
  def put(self,routine_id):
    pass


class DeployManager(Resource):
  """docstring for DeployManager"""
  def __init__(self):
    pass
class DeployListManager(Resource):
  """docstring for DeployListManager"""
  def __init__(self):
    pass
  def get(self):
    return Deploy.objects.to_json()
  def post(self):
    parser=reqparse.RequestParser()
    parser.add_argument("deploy_id",type=str)
    parser.add_argument("user_id",type=str,required=True)
    args=parser.parse_args()
    
    user = User.objects(id=args["user_id"]).get_or_404()
    if args["server_id"]:
      servers = Server.objects(id=request.args.get("server_id"),user=user)
    else:
      servers = Server.objects(user=user)
    for s in servers:
      print s.hostname




class CommandManager(Resource):
  """docstring for CommandManager"""
  def __init__(self):
    pass
class CommandListManager(Resource):
  """docstring for CommandListManager"""
  def __init__(self):
    pass
  def get(self):
    parser=reqparse.RequestParser()
    parser.add_argument("user_id",type=str,required=True)
    parser.add_argument("action",type=str,required=True)
    args=parser.parse_args()

class ServerManager(Resource):
  """docstring for ServerManager"""
  def __init__(self):
    pass
  def get(self,server_id):
    return Server.objects(id=server_id).get_or_404()
     
class ServerListManager(Resource):
  """docstring for ServerListManager"""
  def __init__(self):
    pass
  def post(self):
    parser=reqparse.RequestParser()
    parser.add_argument("hostname",type=str,required=True)
    parser.add_argument("ip",type=str,required=True)
    parser.add_argument("name",type=str,required=True)
    parser.add_argument("user_id",type=str,required=True)
    args=parser.parse_args()
    user=User.objects(id=args["user_id"]).get_or_404()
    server = Server(hostname=args["hostname"],ip=args["ip"],name=args["name"],user=user).save()
    if server:
      return {"message":"server created","id":str(server.id)},201
    else:
      return {"message":"Couldn't create server"},400


class StatusManager(Resource):
  """docstring for StatusManager"""
  def __init__(self):
    pass
class StatusListManager(Resource):
  """docstring for StatusListManager"""
  def __init__(self):
    pass
    
    
#TODO
#to be implemented later because right now i dont have time to do auth and tokens .... :/
class AuthBasicManager(Resource):
  """docstring for AuthBasicManager"""
  def __init__(self, arg):
    super(AuthBasicManager, self).__init__()
    self.arg = arg
  def get(self):
    pass
class AuthKeyManager(Resource):
  """docstring for AuthKeyManager"""
  def __init__(self, arg):
    super(AuthKeyManager, self).__init__()
    self.arg = arg
  def get(self):
    pass
class AuthOauthManager(Resource):
  """docstring for AuthOauthManager"""
  def __init__(self, arg):
    super(AuthOauthManager, self).__init__()
    self.arg = arg
  def get(self):
    pass
    