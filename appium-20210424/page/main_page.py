# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： main_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.contact_page import ContactPage
from page.member_info_page import MemberInfoPage


class MainPage(BasePage):
    __by_contact_lo = (MobileBy.XPATH, '//*[starts-with(@text,"通讯录")]')

    def goto_contact(self):
        self.click_element(self.__by_contact_lo)
        return ContactPage(self.driver)

    def find_member(self, name):
        self.click_element(self.swipe_find_element(name))
        return MemberInfoPage(self.driver)
