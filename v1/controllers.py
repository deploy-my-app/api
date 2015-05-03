from flask import abort
from flask import jsonify
from flask import make_response
from flask import request

from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from v1.models import *
from v1.decorators import *

class UserManager(Resource):
  def __init__(self): #add argument parsor if needed
    self.users=[
      {"id":"1","username":"thomas","password":"pass"}
    ]
    self.keys=[
      {"public_key":"123456789","private_key":"123456789","user_id":"1"}
    ]
  def get(self):
    return {"test":"lol"}

  def authenticate(self,username,password):
    for user in self.users:
      if user["username"] == username and user["password"]==password:
        return True
    return False