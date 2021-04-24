# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： edit_member
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class EditMemberPage(BasePage):
    __del_member_text = '删除成员'
    __del_member_true_lo = (MobileBy.XPATH, '//*[@text="确定"]')
    __del_member_toast_lo = (MobileBy.XPATH, '//*[@text="处理中"]')

    def del_member(self):
        self.click_find_element(self.swipe_find_element(self.__del_member_text))
        self.click_element(self.__del_member_true_lo)
        return self

    def find_toast(self):
        return self.find_element(self.__del_member_toast_lo)
