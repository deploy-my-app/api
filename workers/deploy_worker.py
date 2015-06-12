"""
GET DEPLOYS

FOREACH DEPLOYS
	FOREACH ROUTINE
		FOREACH COMMAND
			IF DEPLOY is SYNCHRONOUS 
				IF COMMAND not in RUNNING_COMMANDS
					IF URL has runned_command AND runned_status is SUCCESS AND URL has deploy_id
						COMMAND = get next command with runned_command
				FOREACH SERVER IN DEPLOY
					ping server.ip?command=COMMAND&ping_back=API_URL
			ELSE_IF DEPLOY NOT SYNCHRONOUS
				ping server.ip?command=COMMAND&ping_back=API_URL
"""
import request,os,sys

class Worker:
	def __init__(self,db,deploy,queue='deploy_queue'):
		self.queue=queue
		self.db=db
		self.deploy=deploy
	def runCommand(self,url):
		r=request.post(url)
	def run(self):
		d=self.deploy
		for r in d.routines:
			for c in r.commands:
				if d.isSyncron:
					if c not in self.db.running_commands.find(command=c)