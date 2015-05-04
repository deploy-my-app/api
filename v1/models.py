from mongoengine.document import Document
from mongoengine.fields import *
from flask.ext.mongoengine import MongoEngine

db =MongoEngine()

class User(Document):
	username = StringField(required=True)
	password = StringField(required=True)

class Key(Document):
	public_key = StringField( required=True, unique=True )
	private_key = StringField( required=True, unique=True )
	user = ReferenceField(User)

class Command(Document):
	action=StringField(required=True)

class Status(Document):
	name=StringField()

class Routine(Document):
	commands=ListField(ReferenceField(Command))
	status = ReferenceField(Status)
	done = BooleanField()
class Server(Document):
	name =StringField(required=True)
	hostname=StringField(required=True)
	ip=StringField(required=True)
	user=ReferenceField(User)

class CommandRoutineStatus(Document):
	server=ReferenceField(Server)
	routine=ReferenceField(Routine)
	command=ReferenceField(Command)
	status=ReferenceField(Status)
	done=BooleanField()
	created_at=DateTimeField()
	finished_at=DateTimeField()
	tries=IntField()
	output=StringField()