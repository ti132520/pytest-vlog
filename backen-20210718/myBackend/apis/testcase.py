from flask import request
from flask_restful import Api, Resource
from model.testcase import Testcase
from server import app, db


class TestcaseService(Resource):
    def get(self):
        """
        获取 testcase
        :return:
        """
        case_id = request.args.get("id")
        if case_id:
            case_data = Testcase.query.filter_by(id=case_id).first()
            data = [case_data.as_dict()]

        else:
            case_data = Testcase.query.all()
            data = [i.as_dict() for i in case_data]
        return {"code": 0, "msg": "success", "data": data}

    def post(self):
        testcase = Testcase()
        # 如果数据字段存在列表，需要做一次转换
        testcase.nodeId = request.json.get("nodeId")
        testcase.remark = request.json.get("remark")
        db.session.add(testcase)
        db.session.commit()
        return {"code": 0, "msg": "post success"}

    def put(self):
        case_data = request.json
        case_id = request.json.get("id")
        old_data = Testcase.query.filter_by(id=case_id).first()
        app.logger.info(old_data)
        if old_data:
            case = Testcase.query.filter_by(id=case_id).update(case_data)
            db.session.commit()

            if case:
                return {"code": 0, "msg": "edit success", "data": case}
            else:
                return {"code": 500, "msg": "put err", "data": case}
        else:
            return {"code": 404, "msg": "no this data"}

    def delete(self):
        case_id = request.json.get("id")
        app.logger.info(request.json.get("id"))
        if not case_id:
            return {"code": 404, "msg": "Delete case_id can't be null."}
        case = Testcase.query.filter_by(id=case_id).delete()
        app.logger.info(case)
        db.session.commit()
        return {"code": 0, 'msg': "delete success."}