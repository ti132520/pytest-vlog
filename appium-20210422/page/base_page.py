# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/22
# File      ： base_page
# IDE       ： PyCharm
from appium import webdriver


class BasePage:
    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            caps = {"platformName": "android", "deviceName": "1", "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.WwMainActivity", "noReset": "true"}
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待5秒
        self.driver.implicitly_wait(5)

    def find_element(self, by, ele=None):
        """
        :param by:
        :param ele:
        :return:
        """
        if ele:
            return self.driver.find_element(by, ele)
        else:
            return self.driver.find_element(*by)

    def click_element(self, by, ele=None):
        """
        :param by:
        :param ele:
        :return:
        """
        if ele:
            return self.driver.find_element(by, ele).click()
        else:
            return self.driver.find_element(*by).click()

    def send_element(self, by, ele=None, val=None):
        """
        :param val:
        :param by:
        :param ele:
        :return:
        """
        if ele:
            return self.driver.find_element(by, ele).send_keys(val)
        else:
            return self.driver.find_element(*by).send_keys(val)

    def find_android_uiautomator(self, ele):
        """
        通过android_uiautomator 查找
        :param ele:
        :return:
        """
        return self.driver.find_element_by_android_uiautomator(ele)

    def click_android_uiautomator(self, ele):
        """
        通过android_uiautomator 查找
        :param ele:
        :return:
        """
        return self.driver.find_element_by_android_uiautomator(ele).click()
