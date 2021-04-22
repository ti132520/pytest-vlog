# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/22
# File      ： conftest
# IDE       ： PyCharm
import pytest

from page.main_page import MainPage


@pytest.fixture(scope='session')
def main_page():
    main_page = MainPage()
    yield main_page
    main_page.quit()
