from server import db


class Testcase(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nodeId = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        return {
            "id": self.id,
            "nodeId": self.nodeId,
            "remark": self.remark
        }


if __name__ == '__main__':
    db.create_all()
