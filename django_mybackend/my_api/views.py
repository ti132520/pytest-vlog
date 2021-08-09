import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from manage import success, error
from my_api.models import TestCase, Task


def testcase(request):
    method = request.method
    if method == 'GET':
        par = request.GET
        if 'id' in par:
            case_data = TestCase.objects.filter(id=par['id'])
        else:
            case_data = TestCase.objects.all()

        if case_data:
            data = [i.as_dict() for i in case_data]
            return success(data)
        else:
            return error('没有数据')
    elif method == 'POST':
        par = json.loads(request.body)
        if 'nodeId' not in par and 'remark' not in par:
            return error('没有数据传入')
        save_data = TestCase(nodeId=par['nodeId'], remark=par['remark'])
        save_data.save()
        return success()
    elif method == 'PUT':
        par = json.loads(request.body)
        if 'nodeId' not in par and 'remark' not in par and 'id' not in par:
            return error('没有数据传入')
        save_data = TestCase.objects.get(id=par['id'])
        if save_data:
            save_data.nodeId = par['nodeId']
            save_data.remark = par['remark']
            save_data.save()
            return success()
        else:
            return error('没有那一条数据')
    elif method == 'DELETE':
        par = json.loads(request.body)
        if 'id' not in par:
            return error('没有传入id')
        delete_data = TestCase.objects.get(id=par['id'])
        if delete_data:
            delete_data.delete()
            return success()
        else:
            return error('没有那一条数据')
    else:
        return error('请求类型错误')


def task(request):
    if request.method == 'GET':
        par = request.GET
        print(par)
        if 'id' in par:
            task_data = Task.objects.filter(id=par['id'])
        else:
            task_data = Task.objects.all()
        if task_data:
            data = [i.as_dict() for i in task_data]
            return success(data)
        else:
            return error('没有数据')
    elif request.method == 'POST':
        pass
    else:
        error('请求类型错误')
