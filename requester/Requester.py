#!/usr/bin/python

import requests,os,sys
from urlparse import urlparse
import hashlib
class ApiRequester(object):
	def __init__(self,user_key,api_key):
		self.request=requests
		self.api_key=api_key
		self.user_key=user_key
	def get(self,resource,**args):
		return self.request.get(self.signRequest(resource),**args,headers=self.header)
	def post(self,resource,**args):
		return self.request.post(self.signRequest(resource),**args,headers=self.header)
	def put(self,resource,**args):
		return self.request.put(self.signRequest(resource),**args,headers=self.header)
	def delete(self,resource,**args):
		return self.request.delete(self.signRequest(resource),**args,headers=self.header)
	def head(self,resource,**args):
		return self.request.head(self.signRequest(resource),**args,headers=self.header)
	def header(self):
		return {
			"user-agent":"Api-Requester/1.0.0"
		}
	def signRequest(self,resource):
		u=urlparse(resource)
		signature=hashlib.sha512(user_key+u.params).hexdigest()
		url=resource
		if u.params:
			url=url+"&user_key="+user_key+"&signature"+signature
		else:
			url=url+"?user_key="+user_key+"&signature"+signature

		self.signature=signature

		return url