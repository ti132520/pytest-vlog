from flask import request
from flask_restful import Api, Resource
from model.task import Task
from server import app, db


class TaskService(Resource):
    def get(self):
        task_id = request.args.get("id")
        if task_id:
            res = Task.query.filter_by(id=task_id).first()
        else:
            res = Task.query.all()
        data = [item.as_dict() for item in res]
        return {"code": 0, "msg": "success", "data": data}

    def post(self):

        return {"code": 0, "msg": "post success"}
