# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： contact_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.add_member_page import AddMemberPage
from page.base_page import BasePage
from page.member_info_page import MemberInfoPage


class ContactPage(BasePage):
    __add_member_text = '添加成员'

    def goto_add_member(self):
        self.click_find_element(self.swipe_find_element(self.__add_member_text))
        return AddMemberPage(self.driver)

    def goto_member_info(self, name: str):
        self.click_find_element(self.swipe_find_element(name))
        return MemberInfoPage(self.driver)
