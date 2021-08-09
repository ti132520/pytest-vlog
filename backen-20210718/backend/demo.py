# 不要看成requests！！！！！！！！！！！！！
from flask import Flask, request

# 路由定义
# 设定请求方法
# 获取请求参数
# 获取请求体


# 实例化flask 对象
app = Flask(__name__)

# 指定路由, 每一次，访问此路由，都会执行方法里面的内容
# 通过methods参数设置请求方法
@app.route("/", methods = ["get", "post"])
# @app.route("/", methods = ["get"])
def hello_world():
    # request.args获取请求url中的参数信息
    id = request.args.get("id")
    # request.json 获取请求体中的数据信息
    return request.json

@app.route("/hogwarts")
def hello_hogwarts():
    return "<p>Hello, hogwarts!</p>"



if __name__ == '__main__':
    # 直接调用app.run 方法 启动后端服务
    # 启动的时候通过port 参数指定端口
    # 当debug = True 的时候，是热加载，方便我们调试后端逻辑
    app.run(debug=True, port=8000)


