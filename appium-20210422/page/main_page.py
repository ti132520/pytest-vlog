# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/22
# File      ： main_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from page.add_member_of_sd_page import AddMemberOfSdPage
from page.base_page import BasePage
from page.contact_page import ContactPage


class MainPage(BasePage):
    __by_contact_lo = (MobileBy.XPATH, '//*[@text="通讯录"]')
    __by_add_member_android_uiautomator = 'new UiScrollable(new UiSelector().scrollable(true).instance(' \
                                          '0)).scrollIntoView(new UiSelector().text("添加成员") .instance(0)) '
    __by_add_member_of_sd_lo = (MobileBy.XPATH, '//*[@text="手动输入添加"]')

    def quit(self):
        self.driver.quit()

    def goto_contact_page(self):
        self.click_element(self.__by_contact_lo)
        return ContactPage(self.driver)

    def goto_add_member_of_sd(self):
        self.click_element(self.__by_contact_lo)
        self.click_android_uiautomator(self.__by_add_member_android_uiautomator)
        self.click_element(self.__by_add_member_of_sd_lo)
        return AddMemberOfSdPage(self.driver)
