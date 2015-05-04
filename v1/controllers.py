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
    return User.objects()
  def post(self):
    args=self.parser.parse_args()
    print args
#Manage a specific User
class UserListManager(Resource):
  """docstring for UserListManager"""
  def __init__(self, arg):
    self.user=User
  def get(self,user_id):
    return self.user.objects(_id=userid).first()
#The holy grail class that will run the core of this huge mess
class CommandStatusManager(Resource):
  """docstring for CommandStatusManager"""
  def __init__(self, arg):
    super(CommandStatusManager, self).__init__()
    self.arg = arg


class RoutineManager(Resource):
  """docstring for RoutineManager"""
  def __init__(self, arg):
    super(RoutineManager, self).__init__()
    self.arg = arg

class RoutineListManager(Resource):
  """docstring for RoutineListManager"""
  def __init__(self, arg):
    super(RoutineListManager, self).__init__()
    self.arg = arg



class DeployManager(Resource):
  """docstring for DeployManager"""
  def __init__(self, arg):
    super(DeployManager, self).__init__()
    self.arg = arg

class DeployListManager(Resource):
  """docstring for DeployListManager"""
  def __init__(self, arg):
    super(DeployListManager, self).__init__()
    self.arg = arg



class CommandManager(Resource):
  """docstring for CommandManager"""
  def __init__(self, arg):
    super(CommandManager, self).__init__()
    self.arg = arg

class CommandListManager(Resource):
  """docstring for CommandListManager"""
  def __init__(self, arg):
    super(CommandListManager, self).__init__()
    self.arg = arg



class ServerManager(Resource):
      """docstring for ServerManager"""
      def __init__(self, arg):
        super(ServerManager, self).__init__()
        self.arg = arg
class ServerListManager(Resource):
  """docstring for ServerListManager"""
  def __init__(self, arg):
    super(ServerListManager, self).__init__()
    self.arg = arg



class StatusManager(Resource):
  """docstring for StatusManager"""
  def __init__(self, arg):
    super(StatusManager, self).__init__()
    self.arg = arg

class StatusListManager(Resource):
  """docstring for StatusListManager"""
  def __init__(self, arg):
    super(StatusListManager, self).__init__()
    self.arg = arg
    
    
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
    