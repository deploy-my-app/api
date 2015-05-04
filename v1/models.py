from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import *
from flask.ext.mongoengine import MongoEngine

db= MongoEngine()
class Key(db.EmbeddedDocument):
	public_key 	= 	db.StringField( required=True )
	private_key	= 	db.StringField( required=True )

class User(db.Document):
	username 	= 	db.StringField(required=True)
	password 	= 	db.StringField(required=True)
	keys 		=	db.ListField(EmbeddedDocumentField(Key))


class Command(db.Document):
	action		=	db.StringField(required=True)

class Status(db.Document):
	name		=	db.StringField()

class Routine(db.Document):
	name 		= 	db.StringField(required=True)
	commands 	=	db.ListField(ReferenceField(Command))
	status 		= 	db.ReferenceField(Status)
	done 		= 	db.BooleanField()

class Server(db.Document):
	name 		=	db.StringField(required=True)
	hostname	=	db.StringField(required=True)
	ip 			=	db.StringField(required=True)
	user 		= 	db.ReferenceField(User)

class CommandRoutineStatus(db.Document):
	server 		=	db.ReferenceField(Server)
	routine 	=	db.ReferenceField(Routine)
	command 	=	db.ReferenceField(Command)
	status 		=	db.ReferenceField(Status)
	done 		=	db.BooleanField()
	created_at 	=	db.DateTimeField()
	finished_at =	db.DateTimeField()
	tries 		=	db.IntField()
	output 		=	db.StringField()