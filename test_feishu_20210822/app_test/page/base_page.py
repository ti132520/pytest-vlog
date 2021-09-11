# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： base_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def swipe_find_element(self, text, num=5):
        """
        滑动查找封装
        :param text: 要查找到的值
        :param num: 找几次
        :return:
        """
        for i in range(0, num):
            try:
                element = self.find_element(MobileBy.XPATH, f'//*[contains(@text,"{text}")]')
                self.driver.implicitly_wait(5)
                return element
            except NoSuchElementException:
                # 屏幕尺寸
                size = self.driver.get_window_size()
                width = size['width']
                start_x = width / 2
                height = size['height']
                start_y = height * 0.8
                stop_x = start_x
                stop_y = height * 0.3
                self.driver.swipe(start_x, start_y, stop_x, stop_y, duration=1000)

            if i == num - 1:
                # 如果达到 num-1次没有找到，则抛出这个异常
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{i}次，未找到")

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

    def click_find_element(self, ele):
        return ele.click()

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

    def find_toast(self, message):
        return WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
