import json

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
CORS(app)
ip = "101.132.153.82"
port = "3306"
username = "testcase"
pwd = "xWB84SJA6kGBHzaN"
database = "testcase"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


def router():
    from apis.testcase import TestcaseService
    api.add_resource(TestcaseService, "/testcase")
    from apis.task import TaskService
    api.add_resource(TaskService, "/task")
def index():
    return {'code':1}

if __name__ == "__main__":
    router()
    api.add_resource(index(), "/")
    app.run(debug=True)
