import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app, supports_credentials=True, origins="*")
username = "root"
pwd = "123456"
ip = "134.175.28.202"
port = "8888"
database = "test_ck18"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 解决warning 问题
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Testcase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        """
        返回一个标准的python 结构体
        :return:
        """
        return {"id": self.id,
                "nodeid": self.nodeid,
                "remark": self.remark}


# 类代表是哪个接口资源，每个方法，代表对此资源的操作，比如 get、post等
# 在类服务中继承resource，表示使用flask-restful
class TestCaseService(Resource):
    """
    测试用例服务
    """

    # 方法名，对应 app.route中的methods
    def get(self):
        """
        查询接口，查询用例数据信息
        """
        # request 获取 接口发过来的请求信息
        case_id = request.args.get("id")
        if case_id:
            # 当传入caseID时，查询单条数据信息
            case_data = Testcase.query.filter_by(id=case_id).first()
            app.logger.info(case_data)
            # data = [{"id": case_data.id, "nodeid": case_data.nodeid, "remark": case_data.remark}]
            data = [case_data.as_dict()]
        else:
            # 反之查询所有的用例信息
            case_data = Testcase.query.all()
            # data = [{"id": i.id, "nodeid": i.nodeid, "remark": i.remark} for i in case_data]
            data = [i.as_dict() for i in case_data]
        return {"error": 0, "msg": {"data": data}}


    def post(self):
        # 增加一条用例
        case_data = request.json
        app.logger.info(case_data)
        # 从接口中拿到的字典数据进行解包，使用关键字传参传入Testcase
        testcase = Testcase(**case_data)
        # 如果数据字段存在列表，需要做一次转换
        testcase.nodeid = json.dumps(request.json.get("nodeid"))
        db.session.add(testcase)
        db.session.commit()
        return {"error": 0, "msg": "post success"}

    def put(self):
        """
        修改接口信息
        :return:
        """
        app.logger.info(request.json)
        # 获取被修改的接口信息
        case_id = request.json.get("id")
        # 通过id 找到要修改的内容， 然后通过update修改对应的数据
        # 找到被修改的接口信息然后做修改操作
        case = Testcase.query.\
            filter_by(id=case_id).\
            update(request.json)
        app.logger.info(f"数据已修改，id{case}被修改为{request.json}")
        # 返回被修改数据的id
        return {"error": 0, "msg": {"id": case}}


    def delete(self):
        """
        删除操作
        :return:
        """
        case_id = request.args.get("id")
        if not case_id:
            return {"error": 40001, "msg": "Delete case_id can't be null"}
        # 返回一个主键
        case = Testcase.query.filter_by(id=case_id).delete()
        db.session.commit()
        app.logger.info(case)
        return {"error": 0, "msg": {"id": case}}


class TaskService(Resource):
    pass


if __name__ == '__main__':
    # 把服务添加到app flask 中
    # 第一个参数是添加的接口服务， 第二个参数，是指定对应接口服务使用的路由
    # db.create_all()
    api.add_resource(TestCaseService, "/testcase")
    # api.add_resource(TaskService, "/task")
    app.run(debug=True)
