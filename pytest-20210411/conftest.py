from typing import List

import pytest
import yaml
from Calculator import Calculator


@pytest.fixture(params=yaml.safe_load(open('testData/par.yaml', 'r')))
def init_calculator_data(request):
    return request.param


@pytest.fixture(scope="function")
def init_calculator_fun():
    cal = Calculator()
    # print('计算开始')
    yield cal
    # print('计算结束')


# hook 收集测试用例后改变一些参数
def pytest_collection_modifyitems(items: List):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")

