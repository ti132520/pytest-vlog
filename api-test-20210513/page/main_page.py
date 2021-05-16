# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/14
# File      ： main_page
# IDE       ： PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class MainPage(BasePage):
    __by_of_search = (By.XPATH, '//*[@id="su"]')
    __by_of_input = (By.XPATH, '//*[@id="kw"]')
    __by_of_frist = (By.XPATH, '//*[@class="t"]/a')

    def search(self, key=None):
        self.send(self.__by_of_search, val=key)

    def get_att(self):
        return self.driver.find_element_by_id("su").get_attribute('value')

    def get_handles(self):
        self.send(self.__by_of_input, val='ssl')
        self.click(self.__by_of_search)
        self.click(self.__by_of_frist)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        sleep(4)
        return handles
