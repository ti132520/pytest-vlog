# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： add_member
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.add_member_of_sd_page import AddMemberOfSdPage
from page.base_page import BasePage


class AddMemberPage(BasePage):
    __by_add_member_of_sd_lo = (MobileBy.XPATH, '//*[contains(@text, "手动输入添加")]')
    __by_toast_lo = (MobileBy.XPATH, '//*[contains(@text, "添加成功")]')

    # 跳转到手动添加成员页面
    def goto_add_member_of_sd(self):
        self.click_element(self.__by_add_member_of_sd_lo)
        return AddMemberOfSdPage(self.driver)

    # 寻找添加成功提示
    def find_toast(self):
        return self.find_element(self.__by_toast_lo)
