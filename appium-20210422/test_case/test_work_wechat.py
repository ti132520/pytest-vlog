# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/22
# File      ： test_work_wechat
# IDE       ： PyCharm
import allure
import pytest
import yaml


class TestWorkWechat:

    @allure.title("测试添加成员")
    @pytest.mark.add_member_of_sd
    @pytest.mark.parametrize('yaml_data', yaml.safe_load(open('data/add_member.yaml', 'r')))
    def test_add_member(self, main_page, yaml_data):
        res = main_page.goto_add_member_of_sd().add_member_of_sd(yaml_data['name'], yaml_data['phone'])
        assert res

