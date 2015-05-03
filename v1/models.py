from mongoengine import *

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
  '''def getRoutineStatus(self,id,server):
    return 
  '''
class Command(object):
  """docstring for Command"""
  def __init__(self, arg):
    super(Command, self).__init__()
    self.arg = arg
  def updateStatus(self,id,statusid):
    c = next((item for item in Commands if item['id'] == id), None)
    c["status_id"]=statusid
    c.save()
  def get(self,id):
    return next((item for item in Commands if item['id'] == id), None)