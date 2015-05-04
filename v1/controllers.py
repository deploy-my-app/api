from flask import abort
from flask import jsonify
from flask import make_response
from flask import request

from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from v1.models import *
from v1.decorators import *




#Manage all users
class UserManager(Resource):
  def __init__(self):
    parser=reqparse.RequestParser()
    parser.add_argument("username",type=str,required=True)
    parser.add_argument("password",type=str,required=True)
    self.parser=parser
    self.users=User
  def get(self):
    return User.objects.only(*["username","id","keys"]).select_related().to_json()
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
class UserListManager(Resource):
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
        raise Exception("The field wasn't found in the user model")
      
      return {"id":str(user["id"]),"username":user["username"]}
    except Exception as e:
      return {"error":e.message},400
    
    
    


#The holy grail class that will run the core of this huge mess
class CommandStatusManager(Resource):
  """docstring for CommandStatusManager"""
  def __init__(self):
    pass
  #retrieves all the details for a command status
  def get(self,deploy_id,server_id,command_id):
    pass
  #creates a new command status
  def post(self,deploy_id,server_id,command_id):
    pass
  #updates a command status
  def put(self,deploy_id,server_id,command_id):
    pass


class RoutineManager(Resource):
  """docstring for RoutineManager"""
  def __init__(self):
    parser=reqparse.RequestParser()
    parser.add_argument("name")
  def get(self):
    return Routine.objects.all().to_json()
  def post(self):
    pass
class RoutineListManager(Resource):
  """docstring for RoutineListManager"""
  def __init__(self):
    pass
  def get(self,routine_id):
    pass
  def patch(self,routine_id):
    pass


class DeployManager(Resource):
  """docstring for DeployManager"""
  def __init__(self):
    pass
class DeployListManager(Resource):
  """docstring for DeployListManager"""
  def __init__(self):
    pass



class CommandManager(Resource):
  """docstring for CommandManager"""
  def __init__(self):
    pass
class CommandListManager(Resource):
  """docstring for CommandListManager"""
  def __init__(self):
    passg



class ServerManager(Resource):
      """docstring for ServerManager"""
      def __init__(self):
        pass
class ServerListManager(Resource):
  """docstring for ServerListManager"""
  def __init__(self):
    pass



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
    