# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： test_work_wechat
# IDE       ： PyCharm
import allure
import pytest
import logging
from page.app import App
from utils.user import User


class TestWorkWechat:
    def setup_class(self):
        logging.basicConfig(level=logging.ERROR,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='appium_test.log',
                            filemode='w')
        self.main = App()

    def teardown_method(self):
        self.main.restart()

    def teardown_class(self):
        self.main.stop()

    @allure.title('测试添加成员')
    @pytest.mark.parametrize("num", [0, 1, 2])
    def test_add_member_of_sd(self, num):
        name = User().get_name()
        phone = User().get_phone()
        logging.info(f'测试添加成员{name}开始')
        with open('data/add_member.yaml', 'a') as f:
            f.write(f'- name: {name}\n  phone: {phone}\n')
            f.close()
        assert self.main.goto_main().goto_contact().goto_add_member()\
            .goto_add_member_of_sd().add_member_of_sd(name, phone).find_toast()

    @allure.title('测试删除成员')
    @pytest.mark.del_member
    @pytest.mark.parametrize('name', ['王敏', '马磊'])
    def test_del_member(self, name):
        logging.info(f'测试删除成员{name}开始')
        assert self.main.goto_main().goto_contact().goto_member_info(name)\
            .goto_member_info_more().goto_edit_member().del_member()
        assert True
