# -*- coding: utf-8 -*-
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： add_member_of_sd
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class AddMemberOfSdPage(BasePage):
    __by_name_lo = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
    __by_phone_lo = (MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText")
    __by_save_lo = (MobileBy.XPATH, "//*[contains(@text,'保存')]")

    def add_member_of_sd(self, name, phone):
        self.send_element(self.__by_name_lo, val=name)
        self.send_element(self.__by_phone_lo, val=phone)
        self.click_element(self.__by_save_lo)
        # 局部引入，避免循环引入
        from page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
