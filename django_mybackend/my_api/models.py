from django.db import models

# Create your models here.


class TestCase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="用例名字", max_length=20, null=True)
    nodeId = models.CharField(verbose_name="node id", max_length=20)
    create_at = models.DateTimeField(verbose_name="新建时间", auto_now_add=True)
    remark = models.CharField(verbose_name="备注", max_length=255)

    class Meta:
        verbose_name_plural = '用例表'

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "nodeId": self.nodeId,
            "remark": self.remark,
            "create_at": str(self.create_at),
        }


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    remark = models.CharField(verbose_name="备注", max_length=255)
    create_at = models.DateTimeField(verbose_name="新建时间", auto_created=True)
    report = models.CharField(verbose_name="报告地址", max_length=255)

    class Meta:
        verbose_name_plural = '任务表'

    def as_dict(self):
        return {
            "id": self.id,
            "remark": self.remark,
            "report": self.report,
            "create_at": str(self.create_at),
        }
