from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import *
from flask.ext.mongoengine import MongoEngine

db= MongoEngine()
class Key(db.EmbeddedDocument):
	public_key 			=	 	db.StringField( required=True )
	
class ApiKey(db.EmbeddedDocument):
	public_key 			= 		db.StringField( required=True )
	private_key			=	 	db.StringField( required=True )

class User(db.Document):
	username 			=	 	db.StringField(required=True)
	password 			=	 	db.StringField(required=True)
	keys 				=		db.ListField(EmbeddedDocumentField(Key))


class Command(db.Document):
	action				=		db.StringField(required=True)

class Status(db.Document):
	name				=		db.StringField()

class Routine(db.Document):
	name 				=	 	db.StringField(required=True)
	commands 			=		db.StringField(required=True) # TODO db.ListField(ReferenceField(Command))

class Server(db.Document):
	name 				=		db.StringField(required=True)
	hostname			=		db.StringField(required=True)
	ip 					=		db.StringField(required=True)
	user 				=	 	db.ReferenceField(User)
	queue 				= 		db.StringField(required=True) #this queue is a string container the rpc_queue_"USER.ID"

class Deploy(db.Document):
	commit 				=	 	db.StringField()
	commit_message 		=	 	db.StringField()
	files 				= 		db.URLField() # url to the tarbal
	routines 			=	 	db.ListField(db.ReferenceField(Routine))
	servers 			=	 	db.ListField(db.ReferenceField(Server))
	user 				= 		db.ReferenceField(User)
	started_at 			=	 	db.DateTimeField()
	ended_at 			=	 	db.DateTimeField()
	

class Job(db.Document):
	uuid 				= 		db.UUIDField()
	command 			=		db.StringField()
	server 				= 		db.ReferenceField(Server)
	deployement 		= 		db.ReferenceField(Deploy)
	status 				=		db.ReferenceField(Status)
	created_at 			=		db.DateTimeField()
	finished_at 		=		db.DateTimeField()
	tries 				=		db.IntField()
	output 				=		db.StringField()