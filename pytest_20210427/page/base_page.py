# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/27
# File      ： base_page
# IDE       ： PyCharm
from appium.webdriver.webdriver import WebDriver


def ele_is_none(by, ele=None):
    if ele:
        res = (by, ele)
        return res
    else:
        return by


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 查找方法
    def find(self, by, ele=None):
        return self.driver.find_element(*ele_is_none(by, ele))

    # 点击方法
    def click(self, by, ele=None):
        return self.driver.find_element(*ele_is_none(by, ele)).click()

    # 滑动方法
    def swipe(self, start_x, start_y, stop_x, stop_y, duration=0):
        """
        滑动
        :param duration: 多少时间内完成滑动，单位ms
        :param start_x: 开始滑动的x与屏幕x的百分比
        :param start_y: 开始滑动位置y与屏幕y的百分比
        :param stop_x: 结束滑动的x与屏幕x的百分比
        :param stop_y: 结束滑动位置y与屏幕y的百分比
        :return:
        """
        size = self.driver.get_window_size()
        width = size.get('width')
        height = size.get('height')
        self.driver.swipe(width * start_x, height*start_y, width*stop_x, height*stop_y, duration)

    # 输入方法
    def send(self, by, ele=None, val=None):
        return self.driver.find_element(*ele_is_none(by, ele)).send_keys(val)
