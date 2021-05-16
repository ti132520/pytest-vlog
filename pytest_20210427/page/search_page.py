# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/28
# File      ： search_page
# IDE       ： PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class SearchPage(BasePage):
    __by_search_lo = (By.XPATH, '//android.EditText')

    def search_keyword(self, key):
        print(self.driver.find_element(*self.__by_search_lo).send_keys(key))
        self.send(self.__by_search_lo, val=key)
        sleep(5)