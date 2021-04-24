# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： member_info_more_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.edit_member_page import EditMemberPage


class MemberInfoMorePage(BasePage):
    __by_edit_member_lo = (MobileBy.XPATH, '//*[@text="编辑成员"]')

    def goto_edit_member(self):
        self.click_element(self.__by_edit_member_lo)
        return EditMemberPage(self.driver)
