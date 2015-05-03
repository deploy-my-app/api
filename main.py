"""
Entry point to our Api
"""
from flask import Flask
from flask.ext import restful

from v1 import deploy

app = Flask(__name__)
api = restful.Api(app)

api.add_resource()


if __name__ == '__main__':
    app.run(debug=True)

