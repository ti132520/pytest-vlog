# -*- coding: utf-8 -*-
# Author    ： 怕你呀
# Time      ： 2021/4/18
# File      ： test_add_member
# IDE       ： PyCharm
import allure
import pytest
import yaml

from test_web_chat.page.main_page import MainPage


class TestAddMember:

    def setup_method(self):
        main_page = MainPage()
        main_page.goto_main1()

    @allure.title("添加成员测试用例")
    @pytest.mark.add_member
    @pytest.mark.parametrize('add_member_data', yaml.safe_load(open('test_web_chat/user_data/add_member.yaml', 'r')))
    def test_add_member(self, add_member_data, main_page):

        # 添加成员
        main_page.goto_add_member().\
            add_member(add_member_data['username'], add_member_data['acctid'], add_member_data['phone'])
        # 获取成员列表
        member_of_phone_list = main_page.goto_contact().get_member_list()
        assert add_member_data['phone'] in member_of_phone_list

    @allure.title("添加成员失败测试用例")
    @pytest.mark.add_member_failed
    @pytest.mark.parametrize('add_member_data', yaml.safe_load(open('test_web_chat/user_data/add_member.yaml', 'r')))
    def test_add_member_failed(self, add_member_data, main_page):
        # 添加成员
        failed_list = main_page.goto_add_member().\
            add_member_failed(add_member_data['username'], add_member_data['acctid'], add_member_data['phone'])
        err = [i for i in failed_list if i != ""]
        assert err[0]


