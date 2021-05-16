# -*- coding: utf-8 -*-
# Author    ： 怕你呀
# Time      ： 2021/4/27
# File      ： main_page
# IDE       ： PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search_page import SearchPage


class MainPage(BasePage):
    __mp_name = '网商助手'
    __by_mp_lo = (By.XPATH, f'//*[contains(@text, "{__mp_name}")]')
    __by_search_lo = (By.XPATH, '//*[contains(@text,"请输入关键字")]')

    def goto_mp(self):
        self.swipe(0.5, 0.3, 0.5, 0.8, 1000)
        self.click(self.__by_mp_lo)
        return self

    def goto_search(self):
        self.click(self.__by_search_lo)
        return SearchPage(self.driver)
