from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 设置flask 关联的数据库
# 使用mysql 进行连接
username = "root"
pwd = "123456"
ip = "134.175.28.202"
# 和启动docker 服务设定的端口保持一致
port = "8888"
database = "test_ck18"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# /tmp/test.db 数据库生成路径
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#
# 数据库关联flask
db = SQLAlchemy(app)

# 一个类表示一张表
class User(db.Model):
    # 每个类属性，表示这个表的表头数据
    # id ， username ， email
    # 在db.Column实例时说明，当前这一列数据的配置
    #               整型， primary_key设置主键
    # 设定表名
    __tablename__ = "client"
    id = db.Column(db.Integer, primary_key=True)
    #  字符串类型，unique 为True代表这一列数据，是不能重复的，都是唯一数据
    #  比如手机号、邮箱的设定， nullable表示，是否可以添加一个为空的数据
    #  如果nullable为False ，代表当前的字段，是不可以为空的
    # db.String(80)表示最长长度 为80
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120))
    # 魔法方法， 打印的时候调用， print、log
    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    # 删除表
    # db.drop_all()
    # 如果表内存放数据，先把数据导出
    # 创建表
    # db.create_all()
    # 增删查改
    ## 增加数据信息
    user2 = User(id=2, username="李五", email="1234@qq.com", gender="男")
    # 把数据对象，添加在session中
    # 对应git commit的操作，可以提交多次
    # db.session.add(user2)
    # db.session.add(user3)
    # 批量添加

    # db.session.add_all([user4, user5])
    # 所有涉及对数据库修改的操作，最后都需要commit 一下
    # 对应 git 的push 操作，所有的修改会提交到数据库
    # db.session.commit()
    ## 查询query,query前面是哪个类，代表，查询哪张表
    # res = User.query.all() # 插叙所有
    ### 条件查询, 我要去查询 id = 1 的时候的数据信息
    # res = User.query.filter_by(gender="男").all()
    # 拿到查询结果的第一条
    # res = User.query.filter_by(gender="男").first()
    # print(res.username, res.email, res.gender)
    # 通过表达式查询
    # res = User.query.all()
    # print(res)
    #删除操作
    # User.query.filter_by(id=2).delete()
    # db.session.commit()
    ## 修改操作
    ### 第一种方法
    # res = User.query.filter_by(id=3).first()
    # 直接修改属性
    # res.gender = "女"
    # db.session.commit()
    ### 第二种方法
    res =User.query.filter_by(id=4).update({"gender": "女", "email": "99@qq.com"})
    # db.session.commit()
