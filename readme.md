small tutorial for large flask application

https://github.com/mitsuhiko/flask/wiki/Large-app-how-to

http://stackoverflow.com/questions/21718603/python-flask-restful-blueprint-and-factory-pattern-work-together

https://github.com/xmm/flask-restful-example

http://flask-restful.readthedocs.org/en/latest/intermediate-usage.html

http://www.antonsetiawan.com/archives/2014/02/using-flask-restful-with-blueprint/

http://flask.pocoo.org/docs/0.10/blueprints/


Every controller in the application is considured a Manager
Every Basic Manager will structure and manage a specific resource Class for the database model, this is used only to update and get propreties of a specific resource
A List manager will structure and manage all resource Class related to it, such as creation of a new resource

to run the application "sudo python run.py"
to use the application in shell "sudo python shell.py"

Use this for creating custom logins with Api Keys

https://flask-login.readthedocs.org/en/latest/

Use Celery for the deploymenet part, so that we can queue all the jobs for each server

https://wiki.openstack.org/wiki/DistributedTaskManagement

https://docs.google.com/presentation/d/185sirdtEzVm59oGAivd7vILeffn6ZeXA22b6PXS1vM4/edit#slide=id.i154