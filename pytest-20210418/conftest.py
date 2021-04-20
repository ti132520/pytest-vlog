# Author    ： 怕你呀
# Time      ： 2021/4/18
# File      ： conftest
# IDE       ： PyCharm
from typing import List


# hook 收集测试用例后改变一些参数
import pytest

from test_web_chat.page.main_page import MainPage


def pytest_collection_modifyitems(items: List):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")


@pytest.fixture(scope='session')
def main_page():
    main_page = MainPage()
    yield main_page
    main_page.quit()
