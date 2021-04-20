# -*- coding: utf-8 -*-
# Author    ： 怕你呀
# Time      ： 2021/4/20
# File      ： test_add_d
# IDE       ： PyCharm
import allure
import pytest
import yaml

from test_web_chat.page.main_page import MainPage


class TestAddDepartment:

    def setup_method(self):

        main_page = MainPage()
        main_page.goto_main1()

    # 测试添加部门
    @allure.title("添加部门测试用例")
    @pytest.mark.test_add_department
    @pytest.mark.parametrize('department_name',
                             yaml.safe_load(open('test_web_chat/user_data/add_departments.yaml', 'r')))
    def test_add_department(self, department_name, main_page):
        department_list = main_page.goto_add_department_page()\
            .add_department(department_name['name']).get_department_list()
        assert department_name['name'] in department_list
