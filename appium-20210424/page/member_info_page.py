# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： member_info_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.member_info_more_page import MemberInfoMorePage


class MemberInfoPage(BasePage):
    __by_member_info_more_lo = (MobileBy.XPATH, '//*[contains(@text, "个人信息")]/../../../../../*[@index=1]')

    def goto_member_info_more(self):
        self.click_find_element(self.find_element(self.__by_member_info_more_lo))
        return MemberInfoMorePage(self.driver)
