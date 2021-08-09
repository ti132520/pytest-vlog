from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        app.logger.warning("get su")
        app.logger.info("get su")
        return {"code": 200, "msg": "su"}

    def post(self):
        app.logger.warning("post su")
        app.logger.info("post su")
        return {"code": 200, "msg": "post su"}

    def put(self):
        app.logger.warning("put su")
        app.logger.info("put su")
        return {"code": 200, "msg": "put  su"}

    def delete(self):
        app.logger.warning("delete su")
        app.logger.info("delete su")
        return {"code": 200, "msg": "delete su"}


if __name__ == '__main__':
    app.run(debug=True)
