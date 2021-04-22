# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/22
# File      ： add_member_of_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.contact_page import ContactPage


class AddMemberOfSdPage(BasePage):
    __by_name_lo = (MobileBy.XPATH, '//*[@id="com.tencent.wework:id/ays"]')
    __by_phone_lo = (MobileBy.XPATH, '//*[@id="com.tencent.wework:id/f4m"]')
    __by_save_lo = (MobileBy.XPATH, '//*[@id="com.tencent.wework:id/ac9"]')
    __by_tips_lo = (MobileBy.XPATH, "//*[@text='手机已存在于通讯录，无法添加']")

    def add_member_of_sd(self, name, phone):
        # 通过上面到定位方法没法定位id 先跳过后期修复
        self.driver.find_element_by_id('com.tencent.wework:id/ays').send_keys(name)
        # self.send_element(self.__by_name_lo, name)
        self.driver.find_element_by_id('com.tencent.wework:id/f4m').send_keys(phone)
        # self.send_element(self.__by_phone_lo, phone)
        self.driver.find_element_by_id('com.tencent.wework:id/ac9').click()
        try:
            self.find_element(self.__by_tips_lo)
        except:
            return True
        return False

